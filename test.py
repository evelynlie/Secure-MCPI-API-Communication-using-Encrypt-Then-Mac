from mcpi_elci_master.mcpi import minecraft
#from mcpi import minecraft

mc = minecraft.Minecraft.create(address="localhost", port=4712)

#[print(bl) for bl in mc.getBlocks(0,0,0,10,10,10)]

mc.postToChat("Hello world")

print("Let's try with other function: mc.getBlock(0,0,0)")
mc.getBlock(0,0,0)