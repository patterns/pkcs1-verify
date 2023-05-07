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
Run verify on the test signature (bottom of `src/mbedcrypto.zig`):
```sh
git clone --recurse-submodules https://github.com/patterns/pkcs1-verify
cd pkcs1-verify
zig build test
```


## Credits

Wrap C lib
 by [Nathan Michaels](https://nmichaels.org/zig/wrap-sodium.html)

Minimal configuration
 by [MbedTLS](https://mbed-tls.readthedocs.io/en/latest/kb/how-to/using-loose-modules-without-the-full-library/)

Example verify
 by [MbedTLS](https://github.com/Mbed-TLS/mbedtls/blob/development/programs/pkey/rsa_verify.c) ([LICENSE](https://github.com/Mbed-TLS/mbedtls/blob/development/LICENSE))


