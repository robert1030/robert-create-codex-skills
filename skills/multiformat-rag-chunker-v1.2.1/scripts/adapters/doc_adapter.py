#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Legacy DOC adapter using a transparent offline LibreOffice conversion."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from adapters.base import AdapterContext
from adapters.docx_adapter import parse as parse_docx
from models import DocumentIR


def parse(path: Path, context: AdapterContext) -> DocumentIR:
    executable = shutil.which("libreoffice") or shutil.which("soffice")
    if not executable:
        return DocumentIR(
            source_id=context.provenance.source_id,
            title=path.stem,
            provenance=context.provenance,
            blocks=[context.block(
                "placeholder",
                "",
                content_origin="placeholder",
                required=True,
                critical=True,
                status="failed",
                verbatim=False,
                metadata={"reason": "libreoffice_not_available_for_doc_conversion"},
            )],
            metadata={"adapter": "doc_adapter"},
            errors=["libreoffice_not_available_for_doc_conversion"],
        )
    output_dir = context.work_dir / "doc-converted"
    output_dir.mkdir(parents=True, exist_ok=True)
    # LibreOffice can fail before conversion when a shared user profile is
    # unavailable or locked.  Keep the profile source-local so concurrent or
    # sandboxed runs do not alter the DOC conversion contract.
    profile_dir = context.work_dir / "libreoffice-profile"
    profile_dir.mkdir(parents=True, exist_ok=True)
    completed = subprocess.run(
        [
            executable,
            f"-env:UserInstallation={profile_dir.as_uri()}",
            "--headless",
            "--convert-to",
            "docx",
            "--outdir",
            str(output_dir),
            str(path),
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
        timeout=120,
    )
    converted = output_dir / f"{path.stem}.docx"
    if completed.returncode != 0 or not converted.is_file():
        return DocumentIR(
            source_id=context.provenance.source_id,
            title=path.stem,
            provenance=context.provenance,
            blocks=[context.block(
                "placeholder",
                "",
                content_origin="placeholder",
                required=True,
                critical=True,
                status="failed",
                verbatim=False,
                metadata={"reason": "doc_conversion_failed", "stderr": completed.stderr},
            )],
            metadata={"adapter": "doc_adapter"},
            errors=["doc_conversion_failed"],
        )
    context.provenance.derivation_chain.append({
        "operation": "libreoffice_doc_to_docx",
        "source": str(path),
        "derived": str(converted),
    })
    document = parse_docx(converted, context)
    document.metadata["adapter"] = "doc_adapter"
    document.metadata["fallback"] = "libreoffice_doc_to_docx"
    return document
