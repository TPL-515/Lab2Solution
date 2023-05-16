# Lab 2

For this lab we will be going over the logging capability within dagster. By the end of the lab you should be able to manipulate the logger in order to send: info updates, warning updates, error updates, etc...

## Getting Started

First clone the lab locally and install the dependencies like so:

```bash
git clone git@github.com:TPL-515/Lab2.git
cd Lab2/
pip install -e ".[dev]"
```

This should install all of the required dependencies for the lab.

## Running the Lab

In order to run the lab just run the following command:

```bash
dagster dev
```

From here you should be able to navigate to the UI hosted at: http://localhost:3000

## Lab Tasks

For this lab you will be asked to perform the following tasks

1) Update the asset to include a logging statement showing off the dimensions of the dummy dataframe

2) Update the asset to include a warning statement if the dataframe has more than 2 rows.

3) Update the asset to include an error statement that throws if the dataframe has more than 2 columns.

4) Update the asset to include a critical error statement if the dataframe has more than 2 rows and two columns.
