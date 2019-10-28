# Claims Consentor Demo
The files in this repo were used to perform a demostration of some features of the Curity Identity Server. In particular, it showed:

* What a claims provider is and how to configure and work with a script claims provider and a consentor claims provider
* What prefix scopes (i.e., dynamic scopes) and how they can be used to avoid scope explosion
* How to seup a BankID signing consentor and how to configure an OAuth client to use that to digitially sign the interactive user consent. Part of this setup was to configure a script that would call a Web service to convert a transaction ID into some text that would be shown to the user for signing.
* How to configure an OAuth client to use these scopes, claims, and digitial signing consentor

The scerio that was demostrated is depicted in the following diagram:

OAuth.tools was used to drive this flow togther with a sample API and the configurtation setup in Curity.
