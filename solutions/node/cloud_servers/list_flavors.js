var pkgcloud = require('pkgcloud'),
    _ = require('underscore');

var client = pkgcloud.providers.rackspace.compute.createClient({
  username: process.env.OS_USERNAME,
  apiKey: process.env.OS_PASSWORD
});

// first we're going to get our flavors
client.getFlavors(function (err, flavors) {
  if (err) {
    console.dir(err);
    return;
  }
  flavors.forEach(function (flavor) {
    console.log("Name: " + flavor.name)
    console.log("  ID: " + flavor.id)
    console.log("  RAM: " + flavor.ram)
    console.log("  Disk: " + flavor.disk)
    console.log("  VCPUs: " + flavor.vcpus)
    console.log()
  })
});
