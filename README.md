# GraphQL-Disjunctive-Union-Parser

Run:</br>
```./main.py```

Returns the disjunctive union of 2 GraphQL files:

Input 1:</br>
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

Input 2:</br>
```
#input Input2 {
#  c2: Int
#  e2: String
#  g2: Boolean
#  h2: [Boolean!]
#}
```

Output:</br>
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