def project_data(profile, config):

    result = {}

    for field in config["fields"]:

        output_name = field["path"]
        source = field["from"]

        if source == "full_name":
            result[output_name] = profile["full_name"]

        elif source == "emails[0]":
            result[output_name] = profile["emails"][0]

        elif source == "skills":
            result[output_name] = profile["skills"]

    if config["include_confidence"]:
        result["_confidence"] = profile["_confidence"]

    return result