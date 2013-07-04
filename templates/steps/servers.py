import os
import pyrax

@then(u'I should have created an "{operating_system}" server with {ram_size} of RAM')
def impl(context, operating_system, ram_size):
    server_id = context.output.strip()
    pyrax.set_setting("identity_type", "rackspace")
    pyrax.set_credentials(os.environ['OS_USERNAME'], os.environ['OS_PASSWORD'])
    cs = pyrax.cloudservers
    import code
    code.interact(local=locals())
    
