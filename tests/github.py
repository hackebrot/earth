import requests
import os
from gidgethub import sansio


def create_issue(owner, repo, title, body, labels):
    request_headers = sansio.create_headers(
        os.environ["ELEPHANT_REQUESTER"], oauth_token=os.environ["ELEPHANT_TOKEN"]
    )

    url = sansio.format_url(
        "/repos/{owner}/{repo}/issues", {"owner": owner, "repo": repo}
    )

    response = requests.post(
        url,
        headers=request_headers,
        json={"title": title, "body": body, "labels": labels},
    )

    data, *_ = sansio.decipher_response(
        response.status_code, response.headers, response.content
    )

    return data
