def parse_disjunctive_union():
    start_of_prune_object_rule = -1

    with open("schema.graphql", "r") as infile, \
            open("schema_out.graphql", "w") as outfile:
        for line in infile:
            exclude_line = False

            if "}\n" in line \
                    or "}" in line:
                start_of_prune_object_rule = -1

            else:
                count = 0

                with open("schema_pruned.graphql", "r") as rules:
                    for rule in rules:
                        if start_of_prune_object_rule == -1 \
                                and "{\n" in line \
                                and line.replace(" ", "") == rule.replace("#", "").replace(" ", ""):
                            start_of_prune_object_rule = count
                            break

                        elif count >= start_of_prune_object_rule:
                            if line.replace(" ", "") == rule.replace("#", "").replace(" ", ""):
                                exclude_line = True

                            elif "}\n" in line \
                                    or "}" in line:
                                break

                        count += 1

            if not exclude_line:
                outfile.write(line)
