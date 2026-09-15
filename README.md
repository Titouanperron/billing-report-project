# Billing Report Project

## Purpose

A team at a fictional company uses this small application to report on generic
billing records. Each row is one invoice with a billed amount and an amount
paid, both in EUR. The report counts invoices and totals the billed and paid
amounts. All identifiers, categories, and amounts are fictional.

Requires Python 3.11 or later. The dataset is included; no online service is needed.

## Initial setup

From the repository root, create and activate a virtual environment.

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Copy `.env.example` to `.env` (`Copy-Item .env.example .env` in PowerShell,
or `cp .env.example .env` on macOS / Linux). Replace the placeholder with the
classroom demo value supplied by your teacher.

This non-sensitive training value is application configuration, separate from
GitHub authentication. The application checks that a value is supplied and that
the placeholder has been replaced; it does not authenticate against a service.
Keep `.env` and `.venv/` local; both are ignored by Git.

## Run

Windows PowerShell:

```powershell
python run.py
```

macOS / Linux:

```bash
python run.py
```

### Alternative: run the module without run.py

From the project root, with dependencies installed and `.env` configured, you can use module execution instead. These commands assume the virtual environment is activated.

Windows PowerShell:

```powershell
$env:PYTHONPATH="src"
python -m billing_app.report
```

macOS / Linux:

```bash
PYTHONPATH=src python -m billing_app.report
```

`PYTHONPATH` tells Python where to find the package in the `src/` layout. In PowerShell, set it again when you open a new terminal. On macOS / Linux, the prefix applies to that command only. Both methods run the same report and require the same local configuration.

If you prefer not to activate the virtual environment, use its Python executable directly:

Windows PowerShell:

```powershell
$env:PYTHONPATH="src"
.\.venv\Scripts\python.exe -m billing_app.report
```

macOS / Linux:

```bash
PYTHONPATH=src ./.venv/bin/python -m billing_app.report
```

## Test

```bash
pytest
```
