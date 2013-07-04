import os
import pyrax

pyrax.set_setting("identity_type", "rackspace")
pyrax.set_credentials(os.environ['OS_USERNAME'], os.environ['OS_PASSWORD'])
cs = pyrax.cloudservers
server_name = 'pyrax_text'
ubu_image = [img for img in cs.images.list()
        if "12.04" in img.name][0]
flavor_512 = [flavor for flavor in cs.flavors.list()
        if flavor.ram == 512][0]

server = cs.servers.create(server_name, ubu_image.id, flavor_512.id)
pyrax.utils.wait_until(server, "status", "ACTIVE", interval=1, attempts=30)
print server.id