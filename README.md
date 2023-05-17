# pkcs1-verify
Learn build configuration in MbedTLS to enable single call: `mbedtls_rsa_pkcs1_verify()`


The #defines for `mbedtls_config.h` required:
```c
    MBEDTLS_ENTROPY_C
    MBEDTLS_HMAC_DRBG_C
    MBEDTLS_MD_C
    MBEDTLS_SHA512_C
    MBEDTLS_SHA256_C
    MBEDTLS_RSA_C
    MBEDTLS_PKCS1_V15
    MBEDTLS_BIGNUM_C
    MBEDTLS_OID_C
    MBEDTLS_ERROR_C
    MBEDTLS_PLATFORM_C
```

## Quickstart
Run verify on the test signature (bottom of `src/pkcs1verify.zig`):
```sh
git clone --recurse-submodules https://github.com/patterns/pkcs1-verify
cd pkcs1-verify
zig build test
```


## Lessons
- Zig dependency currently lacks root CA certs resolution on FreeBSD. Use a CI pipeline such as GitHub workflow inside a Ubuntu image.
- Zig dependency hash currently uses the `sha2-256` multihash. Using a Python script, but also equivalent to combining `sha256sum` CLI with the example Go encode logic.
- Git submodules are not included in the commit-auto tar archives created by GitHub. In order to create a Zig dependency URL, you must generate your own archive file set.
- Zig dependency rejects `.tar.gz` archive. Compared tarballs released on GitHub and GitLab, both are rejected by zig-build. 
- Cirrus CI pipeline task names are hidden when the `only_if: $CIRRUS_BRANCH="main"` rule is applied which prevents dependent tasks during pull requests.
- GitLab CI pipeline uses `$CI_JOB_TOKEN` for the generic package registry; personal access token and project access token are not for the CI x generic package case.

At this time, I think it's necessary to avoid using Git submodules in favor of including the submodule source files directly, and then letting GitHub generate the automatic tar archives. Testing this as next approach for depedency in pink-elephants.

## Credits

Wrap C lib
 by [Nathan Michaels](https://nmichaels.org/zig/wrap-sodium.html)

Minimal configuration
 by [MbedTLS](https://mbed-tls.readthedocs.io/en/latest/kb/how-to/using-loose-modules-without-the-full-library/)

Example verify
 by [MbedTLS](https://github.com/Mbed-TLS/mbedtls/blob/development/programs/pkey/rsa_verify.c) ([LICENSE](https://github.com/Mbed-TLS/mbedtls/blob/development/LICENSE))

Python workflow
 by [Jacob Tomlinson](https://jacobtomlinson.dev/posts/2019/creating-github-actions-in-python/)

MD5 in [Python](https://stackoverflow.com/a/3431838)

