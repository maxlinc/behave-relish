#!/usr/bin/env ruby

# This example demonstrates creating a server with the Rackpace Open Cloud

require 'rubygems' #required for Ruby 1.8.x
require 'fog'
require "base64" #required to encode files for personality functionality

# create Next Generation Cloud Server service
service = Fog::Compute.new({
  :provider             => 'rackspace',
  :rackspace_username   => Fog.credentials[:rackspace_username],
  :rackspace_api_key    => Fog.credentials[:rackspace_api_key],
  :version => :v2,  # Use Next Gen Cloud Servers
  :rackspace_region => :ord #Use Chicago Region
})

# pick the first flavor
flavors = service.flavors
flavors.each do |flv|
  flv.reload
  puts "Name: #{flv.name}"
  puts "  ID: #{flv.id}"
  puts "  RAM: #{flv.ram}"
  puts "  Disk: #{flv.disk}"
  puts "  VCPUs: #{flv.vcpus}"
  puts
end
