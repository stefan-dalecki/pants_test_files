# pants_test_files

An illustrated question about pants file pathing

## Context

This repo is a minimal reprodueable example of an issue that I am facing in my private, commercial codebase (i.e. my day job).

I have unit tests located deep-ish within nested directories. In this example, see `src/tests/dir/subdir/test_example.py`. This test requires data kept in an entirely separate directory, namely `src/tests/test_data/csv/shape_example.csv`. I would like to be able to reference this csv file within `test_example.py`

## Problem

As far as I understand, the [sources](https://www.pantsbuild.org/2.21/docs/using-pants/key-concepts/targets-and-build-files#source-and-sources-field) field requires that `Values are relative to the BUILD file's directory. Sources must be in or below this directory, i.e. ../ is not allowed.`. This seems to be the same case for the `files` field, too. However, this example here is extremely minimal and would be easy to refactor. My codebase has a tremendous amount of test data files (csv, xml, parq, etc...) all within an entirely separate directory than where my test files themselves exist. Refactoring would be a heavy burden.

## Question

Is there a way or workaround to handle my problem? Can I point to data `files` outside the current directory/subdirectory tree of my test modules? I imagine the syntax might look something like this below, but alas, it does not work.

```BUILD

# src/tests/dir/subdir/BUILD

python_tests(
    name="tests",
    dependencies=[":csv_files"]
)

files(name="csv_files", sources=["src/tests/test_data/csv/*.csv"])

```

Conveniently, `pytest` by itself is completely ok with executing `test_example.py`. It will properly detect the .csv file outside the CWD.

```bash
pytest src/tests/dir/subdir/test_example.py
```