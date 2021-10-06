const { execSync } = require("child_process");
const version = process.argv[2];
const dest = process.argv[3];
const tar = require("tar");
const destFile = `${dest}/dist/libstemmer_c-${version}.tar.gz`;

/*
  This builds the libstemmer source at version <$2> from the directory
  specified by <$3>.
*/
execSync("make dist_libstemmer_c", { cwd: dest, shell: true, env: {} });

tar
  .extract({
    file: destFile,
    cwd: `${dest}/dist`,
    onwarn: process.emitWarning,
  })
  .then(() => process.exit(0));

process.on("unhandledRejection", (err) => {
  throw err;
});
