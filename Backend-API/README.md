# Backend-API

## Model Evaluation 
```http
POST https://intellitech-backend.azurewebsites.net/
Params: Essay_Response
```
Response

```javascript
{
  "score" : string,
}
```
## Check Spelling Mistakes 
```http
POST https://intellitech-backend.azurewebsites.net/spelling
Params: Essay_Response
```
Response

```javascript
{
  "score" : string,
}
```
## Total Word Count
```http
POST https://intellitech-backend.azurewebsites.net/words
Params: Essay_Response
```
Response

```javascript
{
  "score" : string,
}
```

## Total Sentence Count
```http
POST https://intellitech-backend.azurewebsites.net/sentences
Params: Essay_Response
```
Response

```javascript
{
  "score" : string,
}
```

## Check Readibility Level
```http
POST https://intellitech-backend.azurewebsites.net/readibility-level
```
Response

```javascript
{
  "Readibility_Level" : string,
}
```
## Check Readibility Grade
```http
POST https://intellitech-backend.azurewebsites.net/readibility-grade
```
Response

```javascript
{
  "Readibility_Grade" : string,
}
```
## Count POS Tags
```http
POST https://intellitech-backend.azurewebsites.net/pos-tags
```
Response

```javascript
{
  'verbs': string,
  'nouns': string,
  'adjectives': string,
  'conjunctions': string,
  'adverbs': string,
  'proper_nouns': string
}
```
## Check Lexical Diversity
```http
POST https://intellitech-backend.azurewebsites.net/lexical-diversity
```
Response

```javascript
{
  'Lexical_Diversity': string,
}
```
## Check Capitalization Errors
```http
POST https://intellitech-backend.azurewebsites.net/capitalization
```
Response

```javascript
{
  'Capitalization_Mistakes': string,
}
```
