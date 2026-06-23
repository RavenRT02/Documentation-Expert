:::: {#security-warnings}

::::

# Security Considerations

The following modules have specific security considerations:

- `base64`:
  `base64 security considerations <base64-security>` in `4648`
- `hashlib`:
  `all constructors take a "usedforsecurity" keyword-only
  argument disabling known insecure and blocked algorithms
  <hashlib-usedforsecurity>`
- `http.server` is not suitable for
  production use, only implementing basic security checks. See the
  `security considerations <http.server-security>`.
- `logging`:
  `Logging configuration uses eval()
  <logging-eval-security>`
- `multiprocessing`:
  `Connection.recv() uses pickle
  <multiprocessing-recv-pickle-security>`
- `pickle`:
  `Restricting globals in pickle <pickle-restrict>`
- `random` shouldn\'t be used for security
  purposes, use `secrets` instead
- `shelve`:
  `shelve is based on pickle and thus unsuitable for
  dealing with untrusted sources <shelve-security>`
- `ssl`:
  `SSL/TLS security considerations <ssl-security>`
- `subprocess`:
  `Subprocess security considerations
  <subprocess-security>`
- `tempfile`:
  `mktemp is deprecated due to vulnerability to race
  conditions <tempfile-mktemp-deprecated>`
- `xml`:
  `XML security <xml-security>`
- `zipfile`:
  `maliciously prepared .zip files can cause disk volume
  exhaustion <zipfile-resources-limitations>`

The `-I` command line option can be
used to run Python in isolated mode. When it cannot be used, the
`-P` option or the
`PYTHONSAFEPATH` environment variable
can be used to not prepend a potentially unsafe path to
`sys.path` such as the current directory,
the script\'s directory or an empty string.