def parse_disjunctive_union():
    inside_pruned_input = False

    with open("schema.graphql", "r") as infile, \
            open("schema_out.graphql", "w") as outfile:
        for line in infile:
            exclude_line = False

            if line == "}\n" or line == "}":
                inside_pruned_input = False

            else:
                with open("schema_pruned.graphql", "r") as rules:
                    for rule in rules:
                        if "{" in line and line.replace(" ", "") == rule.replace("#", "").replace(" ", ""):
                            inside_pruned_input = True
                            break

                        elif inside_pruned_input and line.replace(" ", "") == rule.replace("#", "").replace(" ", ""):
                            exclude_line = True

            if not exclude_line:
                outfile.write(line)
