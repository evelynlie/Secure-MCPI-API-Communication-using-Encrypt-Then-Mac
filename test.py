from mcpi_elci_master.mcpi import minecraft

mc = minecraft.Minecraft.create(address= 'localhost', port= 4712)

mc.getBlocks(0,0,0,10,10,10)