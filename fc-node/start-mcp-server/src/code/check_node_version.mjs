// check-node-version.mjs
import semver from 'semver';
import process from 'process';

const MIN_VERSION = '20.0.0';

try {
  const current = process.version;
  if (semver.lt(current, MIN_VERSION)) {
    console.error(`error：Need Node.js ${MIN_VERSION} or higher version (current version: ${current})`);
    process.exit(1);
  }
  console.log(`Node version check pass: ${current}`);
} catch (error) {
  console.error('Node version check failure: ', error.message);
  process.exit(1);
}
