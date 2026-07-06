# iTest Runtime: iTestRT > iTestRT command reference > NTAF automation: Running test cases that include NTAF sessions > 第1段

To execute an NTAF test case using iTestRT, first start the Spirent NTAF proxy, and then connect to the NTAF server using the NTAF options. For example:

```
iTestRt --itar file:/c:/iTestRt --test project://my_project/TestCases/NtafAvTest42.fftc --ntaf.server crt-fm5q1 --login itestrt --ntaf.password mypassword
```

Note Use a single slash character after “file:” in the URI. For example:

Note

Note The logic of the following values seems reversed, but the following descriptions are correct:

Note Use a single slash character after “file:” in the URI. For example:

Note The credentials represent iTest as a client on the NTAF server. Remember that the Proxy service is a different client on the NTAF server and therefore has a different username.

Note The logic of the following values seems reversed, but the following descriptions are correct:
