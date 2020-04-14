# boolean-retrieval-model
The (standard) Boolean model of information retrieval (BIR) is a classical information retrieval (IR) model and, at the same time, the first and most-adopted one. It is used by many IR systems to this day. The BIR is based on Boolean logic and classical set theory in that both the documents to be searched and the user's query are conceived as sets of terms. Retrieval is based on whether or not the documents contain the query terms.

## Exact vs Best match
In exact match a query specifies precise criteria. Each document either matches or fails to match the query. The results retrieved in exact match is a set of document (without ranking).

In best match a query describes good or best matching documents. In this case the result is a ranked list of document. 

The Boolean model here dealt with is the most common exact match model.

## Basic Assumption of Boolean Model:

* An index term is either present(1) or absent(0) in the document
* All index terms provide equal evidence with respect to information needs.
* Queries are Boolean combinations of index terms.
  * X AND Y: represents doc that contains both X and Y
  * X OR Y: represents doc that contains either X or Y
  * NOT X: represents the doc that do not contain X

## Boolean Queries Example
- User information need: Interested to know about Everest and Nepal.
- User Boolean query: Everest AND Nepal
