const { https } = require("follow-redirects");
const fs = require("fs");
const tar = require("tar");

const version = process.argv[2];
const dest = process.argv[3];
const source = `https://github.com/snowballstem/snowball/archive/refs/tags/v${version}.tar.gz`;
const destFile = `${dest}/snowball-${version}.tar.gz`;

const file = fs.createWriteStream(destFile);

function extract() {
	tar.extract({
		strip: 1,
		file: destFile,
		cwd: dest,
		onwarn: process.emitWarning,
	}).then(() => process.exit(0));
}

/*
	This downloads libstemmer at the version <$2> and places the resulting
	files into the directory specified by <$3>.
 */
https
	.get(source, (response) => {
		response.pipe(file);
		file.on("finish", () => {
			file.close(extract);
		});
	})
	.on("error", (err) => {
		console.error(err.message);
		fs.unlink(dest, () => {
			process.exit(1);
		});
	});

process.on("unhandledRejection", (err) => {
	throw err;
});
