# GraphQL-Disjunctive-Union-Parser

This tool was created to combat schemas with birdirectional relationships that certain code gen libraies would spin on forever. It became part of our workflow to pull the schema and drop unused fields that would cause recursive behavior by hand. This tool significantly improved our process

1. Replace schema.graphql with the entirety of your schema</br>
2. Replace schema-pruned.graphql with the fields nested inside the objects you want them removed from (#'s optional)</br>
3. Run: ```./main.py```
4. Receive disjunctive union of the 2 files in schema-out.graphql</br></br>

Returns the disjunctive union of 2 GraphQL files:

Input 1 (schema.graphql):</br>
```
input Input1 {
  a1: ID
  b1: [ID!]
  c1: Int
  d1: [Int!]
  e1: String
  f1: [String!]
  g1: Boolean
  h1: [Boolean!]
}

input Input2 {
  a2: ID
  b2: [ID!]
  c2: Int
  d2: [Int!]
  e2: String
  f2: [String!]
  g2: Boolean
  h2: [Boolean!]
}
```

Input 2 (schema-pruned.graphql):</br>
```
#input Input2 {
#  c2: Int
#  e2: String
#  g2: Boolean
#  h2: [Boolean!]
#}
```

Output (schema-out.graphql):</br>
```
input Input1 {
  a1: ID
  b1: [ID!]
  c1: Int
  d1: [Int!]
  e1: String
  f1: [String!]
  g1: Boolean
  h1: [Boolean!]
}

input Input2 {
  a2: ID
  b2: [ID!]
  d2: [Int!]
  f2: [String!]
}
```
