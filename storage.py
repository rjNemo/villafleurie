from whitenoise import CompressedManifestStaticFiles


class WhiteNoiseStaticFiles(CompressedManifestStaticFiles):
    manifest_strict = False
