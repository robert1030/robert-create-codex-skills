# Python Session Level Control Library > Working with Sessions > Invoking Actions on Session > Queries

The response object may also have queries defined on it - methods that query the structured data and return values. Queries may be auto-generated in iTest or be defined in response maps.

```
# list the set of queries that exist for the response
```

```
response.queries()
```

```
==> [ 'is_empty()', 'counter_by_row(row)' ]
```

```
# invoke query
```

```
response.counter_by_row(3)
```

```
==> 35
```

> **Note：** Note Query names are always converted to snake case.
