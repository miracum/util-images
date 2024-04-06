# util-images

Collection of container images

## Add a new image

1. Create a folder with the image name below `images/`.
   The name of the folder will also be used as the image name so
   it should only consist of DNS-safe characters and underscores.
1. Add a `Dockerfile` to this folder.
1. Update [ci.yaml](.github/workflows/ci.yaml) and add this folder
   name to the `jobs.build.strategy.matrix.image` array.
1. Update [schedule.yaml](.github/workflows/schedule.yaml) and add this folder
   name to the `jobs.schedule.with.images` array.
1. Update [.release-please-manifest.json](.release-please-manifest.json) with
   the new image and initial version.
1. Update [release-please-config.json](release-please-config.json) and add the image
   to the `packages` section.
