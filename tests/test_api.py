import runcurl


def test_basic_get():
    runcurl.parse("curl 'https://pypi.python.org/pypi/rruncurl'").should.equal(
            """requests.get("https://pypi.python.org/pypi/rruncurl",
        headers={},
        cookies={},
    )"""
    )


def test_basic_headers():
    runcurl.parse(
        "curl 'https://pypi.python.org/pypi/rruncurl' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Accept-Language: en-US,en;q=0.8'").should.equal(
            """requests.get("https://pypi.python.org/pypi/rruncurl",
    headers={
        "Accept-Encoding": "gzip,deflate,sdch",
        "Accept-Language": "en-US,en;q=0.8",
    },
    cookies={},
)"""
    )


def test_cookies():
    runcurl.parse(
        "curl 'https://pypi.python.org/pypi/rruncurl' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Cookie: foo=bar; baz=baz2'").should.equal(
            """requests.get("https://pypi.python.org/pypi/rruncurl",
    headers={
        "Accept-Encoding": "gzip,deflate,sdch",
    },
    cookies={
        "baz": "baz2",
        "foo": "bar",
    },
)"""
    )


def test_cookies_lowercase():
    runcurl.parse(
        "curl 'https://pypi.python.org/pypi/rruncurl' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'cookie: foo=bar; baz=baz2'").should.equal(
            """requests.get("https://pypi.python.org/pypi/rruncurl",
    headers={
        "Accept-Encoding": "gzip,deflate,sdch",
    },
    cookies={
        "baz": "baz2",
        "foo": "bar",
    },
)"""
    )


def test_post():
    runcurl.parse(
        """curl 'https://pypi.python.org/pypi/rruncurl' --data '[{"evt":"newsletter.show","properties":{"newsletter_type":"userprofile"},"now":1396219192277,"ab":{"welcome_email":{"v":"2","g":2}}}]' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Cookie: foo=bar; baz=baz2'""").should.equal(
            """requests.post("https://pypi.python.org/pypi/rruncurl",
    data='[{"evt":"newsletter.show","properties":{"newsletter_type":"userprofile"},"now":1396219192277,"ab":{"welcome_email":{"v":"2","g":2}}}]',
    headers={
        "Accept-Encoding": "gzip,deflate,sdch",
    },
    cookies={
        "baz": "baz2",
        "foo": "bar",
    },
)"""
    )


def test_post_with_dict_data():
    runcurl.parse(
        """curl 'https://pypi.python.org/pypi/rruncurl' --data '{"evt":"newsletter.show","properties":{"newsletter_type":"userprofile"}}' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Cookie: foo=bar; baz=baz2'""").should.equal(
            """requests.post("https://pypi.python.org/pypi/rruncurl",
    data={
        "evt": "newsletter.show",
        "properties": {
            "newsletter_type": "userprofile",
        },
    },
    headers={
        "Accept-Encoding": "gzip,deflate,sdch",
    },
    cookies={
        "baz": "baz2",
        "foo": "bar",
    },
)"""
    )


def test_post_with_string_data():
    runcurl.parse("""curl 'https://pypi.python.org/pypi/rruncurl' --data 'this is just some data'""").should.equal(
            """requests.post("https://pypi.python.org/pypi/rruncurl",
    data='this is just some data',
    headers={},
    cookies={},
)"""
    )


def test_parse_curl_with_binary_data():
    runcurl.parse("""curl 'https://pypi.python.org/pypi/rruncurl' --data-binary 'this is just some data'""").should.equal(
            """requests.post("https://pypi.python.org/pypi/rruncurl",
    data='this is just some data',
    headers={},
    cookies={},
)"""
    )


def test_execute_get():
    print runcurl.execute("curl 'https://pypi.python.org/pypi/runcurl'").status_code == 200