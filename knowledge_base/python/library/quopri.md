# `!quopri` \-\-- Encode and decode MIME quoted-printable data

::: {.module synopsis="Encode and decode files using the MIME quoted-printable encoding."}
quopri
:::

**Source code:** `Lib/quopri.py`

This module performs quoted-printable transport encoding and decoding,
as defined in `1521`: \"MIME (Multipurpose
Internet Mail Extensions) Part One: Mechanisms for Specifying and
Describing the Format of Internet Message Bodies\". The quoted-printable
encoding is designed for data where there are relatively few
nonprintable characters; the base64 encoding scheme available via the
`base64` module is more compact if there
are many such characters, as when sending a graphics file.

::: function
decode(input, output, header=False)

Decode the contents of the *input* file and write the resulting decoded
binary data to the *output* file. *input* and *output* must be
`binary file objects
<file object>`. If the optional argument
*header* is present and true, underscore will be decoded as space. This
is used to decode \"Q\"-encoded headers as described in
`1522`: \"MIME (Multipurpose Internet Mail
Extensions) Part Two: Message Header Extensions for Non-ASCII Text\".
:::

::: function
encode(input, output, quotetabs, header=False)

Encode the contents of the *input* file and write the resulting
quoted-printable data to the *output* file. *input* and *output* must be
`binary file objects <file object>`.
*quotetabs*, a non-optional flag which controls whether to encode
embedded spaces and tabs; when true it encodes such embedded whitespace,
and when false it leaves them unencoded. Note that spaces and tabs
appearing at the end of lines are always encoded, as per
`1521`. *header* is a flag which controls
if spaces are encoded as underscores as per `1522`.
:::

::: function
decodestring(s, header=False)

Like `decode`, except that it accepts a
source `bytes` and returns the
corresponding decoded `bytes`.
:::

::: function
encodestring(s, quotetabs=False, header=False)

Like `encode`, except that it accepts a
source `bytes` and returns the
corresponding encoded `bytes`. By
default, it sends a `False` value to *quotetabs* parameter of the
`encode` function.
:::

::: seealso

Module `base64`

: Encode and decode MIME base64 data
:::