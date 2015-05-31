$setup = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive apt-get update
SCRIPT

$dependencies = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive apt-get install -y postgresql libpq-dev
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-dev libjpeg-dev zlib1g-dev
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-virtualenv virtualenvwrapper
    DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs npm
    DEBIAN_FRONTEND=noninteractive ln -s /usr/bin/nodejs /usr/bin/node
    DEBIAN_FRONTEND=noninteractive apt-get install -y ruby-dev
SCRIPT

$grunt = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive npm install grunt 
    DEBIAN_FRONTEND=noninteractive npm install -g grunt-cli
    DEBIAN_FRONTEND=noninteractive gem install compass    
SCRIPT

Vagrant.configure('2') do |config|

    config.vm.box = 'ubuntu/trusty64'
    #config.vm.box_url = "http://files.vagrantup.com/" + config.vm.box + ".box"

    config.vm.provider "virtualbox" do |vb|
     # Use VBoxManage to customize the VM. For example to change memory:
     vb.customize ["modifyvm", :id, "--memory", "1024"]
    end

    config.ssh.forward_agent = true
    # Forward the dev server port
    config.vm.network :forwarded_port, host: 8000, guest: 8000
    config.vm.network "forwarded_port", guest: 5432, host: 5432
    config.vm.network "forwarded_port", guest: 35729, host: 35729
    
    config.vm.provision "shell", inline: $setup
    config.vm.provision "shell", inline: $dependencies
    config.vm.provision "shell", inline: $grunt
end
