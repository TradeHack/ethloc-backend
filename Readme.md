# Letter of Credit on Ethereum

Hey there :wave:

As part of the [Scaling Ethereum Hackathon](https://hack.ethglobal.co/), @re-minder, @connerjason, and @ajascha decided to build a prototype for a major piece of trade finance to the blockchain: The Letter of Credit.

## Stack

- **Blockchain:** We use [Starkware](https://starkware.co/) for building a scalable Layer 2 application on Ethereum.
- **Frontend:** [Bulma](https://bulma.io)
- **Backend:** [FastAPI](https://fastapi.tiangolo.com)

## Run locally

1. Install [pipenv](https://pipenv-fork.readthedocs.io/)
2. Clone repository
3. Run `pipenv install` to install dependencies
4. Run `uvicorn main:app --reload` to start a local server