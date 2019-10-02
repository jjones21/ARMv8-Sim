
import sys, Queue

class ArmDecode:
    opcodeStr = []
    instrSpaced = []
    arg1 = []
    arg2 = []
    arg3 = []
    arg1Str = []
    arg2Str = []
    arg3Str = []
    mem = []
    binMem = []
    opcode = []
    instForm = []
    dataStart = 0
    dataEnd = 0
    outputFileName = ''
    opcodeSpace = []

    #def __init__(self):


    def run(self):


        opcodeMask = 0xFFE00000 #R format opcode
        rnMask = 0x3E0          #1st argument Arm Rn
        rmMask = 0x1F0000       #second argument ARM Rm
        rdMask = 0x1F           #destination ARM Rd
        imMask = 0x3FFC00       #ARM I Immediate
        shmtMask = 0xFC00       #ARM ShAMT
        addrMask = 0x1FF000     #ARM address for ld and st
        addr2Mask = 0xFFFFE0    #addr for CB format
        imsftMask = 0x600000    #shift for IM format
        imdataMask = 0x1FFFE0   #data for IM type
        breakMask = 0x1FFFFF    #mask for break
        branchMask = 0x03FFFFFF #branch address

        extra = 0
        broken = 0

        for i in range(len(sys.argv)):
            if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
                inputFileName = sys.argv[i + 1]
                print inputFileName

            elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):
                self.outputFileName = sys.argv[i + 1]
                outputFileName2 = self.outputFileName + '_dis.txt'

        inFile = open(inputFileName, 'r')
        outFile = open(outputFileName2, 'w')
        i=0


        with open(inputFileName) as f:
            for line in f:

                masked = int(line, 2) & opcodeMask
                masked = masked >> 21

                if(broken == 0):
                    if masked == 1112: #ADD
                        #---------read----------
                        self.opcode.append(masked)
                        self.opcodeStr.append("ADD")
                        self.arg1.append(int(line, 2) & rdMask)
                        self.arg2.append((int(line, 2) & rnMask) >> 5)
                        self.arg3.append((int(line, 2) & rmMask) >> 16)
                        self.opcodeSpace.append("\t")
                        self.arg1Str.append("\tR" + str(self.arg1[i]))
                        self.arg2Str.append(", R" + str(self.arg2[i]))
                        self.arg3Str.append(", R" + str(self.arg3[i]))

                        #----------print----------
                        self.instrSpaced.append(self.bin2StringSpacedR(line))
                        #print opcode[i]," ",arg2[i]," 000000 ",arg1[i]," ",arg3[i]

                    elif masked == 1624: #SUB
                        # ---------read----------
                        self.opcode.append(masked)
                        self.opcodeStr.append("SUB")
                        self.arg1.append(int(line, 2) & rdMask)
                        self.arg2.append((int(line, 2) & rnMask) >> 5)
                        self.arg3.append((int(line, 2) & rmMask) >> 16)
                        self.opcodeSpace.append("\t")
                        self.arg1Str.append("\tR" + str(self.arg1[i]))
                        self.arg2Str.append(", R" + str(self.arg2[i]))
                        self.arg3Str.append(", R" + str(self.arg3[i]))
                        self.instrSpaced.append(self.bin2StringSpacedR(line))

                    elif masked == 1691: #LSL
                        # ---------read----------
                        self.opcode.append(masked)
                        self.opcodeStr.append("LSL")
                        self.arg1.append(int(line, 2) & rdMask)
                        self.arg2.append((int(line, 2) & rnMask) >> 5)
                        self.arg3.append((int(line, 2) & shmtMask) >> 10)
                        self.opcodeSpace.append("\t")
                        self.arg1Str.append("\tR" + str(self.arg1[i]))
                        self.arg2Str.append(", R" + str(self.arg2[i]))
                        self.arg3Str.append(", #" + str(self.arg3[i]))
                        self.instrSpaced.append(self.bin2StringSpacedR(line))

                    elif masked == 1690: #LSR
                        # ---------read----------
                        self.opcode.append(masked)
                        self.opcodeStr.append("LSR")
                        self.arg1.append(int(line, 2) & rdMask)
                        self.arg2.append((int(line, 2) & rnMask) >> 5)
                        self.arg3.append((int(line, 2) & shmtMask) >> 10)
                        self.opcodeSpace.append("\t")
                        self.arg1Str.append("\tR" + str(self.arg1[i]))
                        self.arg2Str.append(", R" + str(self.arg2[i]))
                        self.arg3Str.append(", #" + str(self.arg3[i]))
                        self.instrSpaced.append(self.bin2StringSpacedR(line))

                    elif masked == 1692: #ASR
                        # ---------read----------
                        self.opcode.append(masked)
                        self.opcodeStr.append("ASR")
                        self.arg1.append(int(line, 2) & rdMask)
                        self.arg2.append((int(line, 2) & rnMask) >> 5)
                        self.arg3.append((int(line, 2) & shmtMask) >> 10)
                        self.opcodeSpace.append("\t")
                        self.arg1Str.append("\tR" + str(self.arg1[i]))
                        self.arg2Str.append(", R" + str(self.arg2[i]))
                        self.arg3Str.append(", #" + str(self.arg3[i]))
                        self.instrSpaced.append(self.bin2StringSpacedR(line))

                    elif masked == 1104: #AND
                        # ---------read----------
                        self.opcode.append(masked)
                        self.opcodeStr.append("AND")
                        self.arg1.append(int(line, 2) & rdMask)
                        self.arg2.append((int(line, 2) & rnMask) >> 5)
                        self.arg3.append((int(line, 2) & rmMask) >> 16)
                        self.opcodeSpace.append("\t")
                        self.arg1Str.append("\tR" + str(self.arg1[i]))
                        self.arg2Str.append(", R" + str(self.arg2[i]))
                        self.arg3Str.append(", R" + str(self.arg3[i]))
                        self.instrSpaced.append(self.bin2StringSpacedR(line))

                    elif masked == 1360: #ORR
                        # ---------read----------
                        self.opcode.append(masked)
                        self.opcodeStr.append("ORR")
                        self.arg1.append(int(line, 2) & rdMask)
                        self.arg2.append((int(line, 2) & rnMask) >> 5)
                        self.arg3.append((int(line, 2) & rmMask) >> 16)
                        self.opcodeSpace.append("\t")
                        self.arg1Str.append("\tR" + str(self.arg1[i]))
                        self.arg2Str.append(", R" + str(self.arg2[i]))
                        self.arg3Str.append(", R" + str(self.arg3[i]))
                        self.instrSpaced.append(self.bin2StringSpacedR(line))

                    elif masked == 1872: #EOR
                        # ---------read----------
                        self.opcode.append(masked)
                        self.opcodeStr.append("EOR")
                        self.arg1.append(int(line, 2) & rdMask)
                        self.arg2.append((int(line, 2) & rnMask) >> 5)
                        self.arg3.append((int(line, 2) & rmMask) >> 16)
                        self.opcodeSpace.append("\t")
                        self.arg1Str.append("\tR" + str(self.arg1[i]))
                        self.arg2Str.append(", R" + str(self.arg2[i]))
                        self.arg3Str.append(", R" + str(self.arg3[i]))
                        self.instrSpaced.append(self.bin2StringSpacedR(line))


                    elif (masked == 2038):  # BREAK
                        # ---------read----------
                        self.opcode.append(masked)
                        self.opcodeStr.append("BREAK")
                        self.arg1.append((int(line, 2) & breakMask))
                        self.arg2.append(0)
                        self.arg3.append(0)
                        self.opcodeSpace.append("")
                        self.arg1Str.append("")
                        self.arg2Str.append("")
                        self.arg3Str.append("")
                        self.instrSpaced.append(self.bin2StringSpacedBreak(line))
                        broken = 1
                        self.dataStart = i
                        self.dataEnd = i

                    elif masked == 1986: #LDUR
                        # ---------read----------
                        self.opcode.append(masked)
                        self.opcodeStr.append("LDUR")
                        self.arg1.append((int(line, 2) & rdMask))
                        self.arg2.append((int(line, 2) & rnMask) >> 5)
                        self.arg3.append((int(line, 2) & addrMask) >> 12)
                        self.opcodeSpace.append("")
                        self.arg1Str.append("\tR" + str(self.arg1[i]))
                        self.arg2Str.append(", [R" + str(self.arg2[i]))
                        self.arg3Str.append(", #" + str(self.arg3[i])+"]")
                        self.instrSpaced.append(self.bin2StringSpacedD(line))

                    elif masked == 1984: #STUR
                        # ---------read----------
                        self.opcode.append(masked)
                        self.opcodeStr.append("STUR")
                        self.arg1.append((int(line, 2) & rdMask))
                        self.arg2.append((int(line, 2) & rnMask) >> 5)
                        self.arg3.append((int(line, 2) & addrMask) >> 12)
                        self.opcodeSpace.append("")
                        self.arg1Str.append("\tR" + str(self.arg1[i]))
                        self.arg2Str.append(", [R" + str(self.arg2[i]))
                        self.arg3Str.append(", #" + str(self.arg3[i]) + "]")
                        self.instrSpaced.append(self.bin2StringSpacedD(line))

                    elif (masked >= 1160) & (masked <= 1161): #ADDI
                        # ---------read----------
                        self.opcode.append(masked>>1)
                        self.opcodeStr.append("ADDI")
                        self.arg1.append((int(line, 2) & rdMask))
                        self.arg2.append((int(line, 2) & rnMask) >> 5)
                        self.arg3.append((int(line, 2) & imMask) >> 10)
                        self.opcodeSpace.append("")
                        self.arg1Str.append("\tR" + str(self.arg1[i]))
                        self.arg2Str.append(", R" + str(self.arg2[i]))
                        self.arg3Str.append(", #" + str(self.arg3[i]))
                        self.instrSpaced.append(self.bin2StringSpacedI(line))

                    elif (masked >= 1672) & (masked <= 1673): #SUBI
                        # ---------read----------
                        self.opcode.append(masked>>1)
                        self.opcodeStr.append("SUBI")
                        self.arg1.append((int(line, 2) & rdMask))
                        self.arg2.append((int(line, 2) & rnMask) >> 5)
                        self.arg3.append((int(line, 2) & imMask) >> 10)
                        self.opcodeSpace.append("")
                        self.arg1Str.append("\tR" + str(self.arg1[i]))
                        self.arg2Str.append(", R" + str(self.arg2[i]))
                        self.arg3Str.append(", #" + str(self.arg3[i]))
                        self.instrSpaced.append(self.bin2StringSpacedI(line))

                    elif (masked >= 1684) & (masked <= 1687):  # MOVZ
                        # ---------read----------
                        self.opcode.append(masked>>2)
                        self.opcodeStr.append("MOVZ")
                        self.arg1.append((int(line, 2) & rdMask))
                        self.arg2.append((int(line, 2) & imdataMask) >> 5)
                        self.arg3.append(((int(line, 2) & imsftMask) >> 21)*16)
                        self.opcodeSpace.append("")
                        self.arg1Str.append("\tR" + str(self.arg1[i]))
                        self.arg2Str.append(", " + str(self.arg2[i]))
                        self.arg3Str.append(", LSL " + str(self.arg3[i]))
                        self.instrSpaced.append(self.bin2StringSpacedIM(line))

                    elif (masked >= 1940) & (masked <= 1943):  # MOVK
                        # ---------read----------
                        self.opcode.append(masked>>2)
                        self.opcodeStr.append("MOVK")
                        self.arg1.append((int(line, 2) & rdMask))
                        self.arg2.append((int(line, 2) & imdataMask) >> 5)
                        self.arg3.append(((int(line, 2) & imsftMask) >> 21)*16)
                        self.opcodeSpace.append("")
                        self.arg1Str.append("\tR" + str(self.arg1[i]))
                        self.arg2Str.append(", " + str(self.arg2[i]))
                        self.arg3Str.append(", LSL " + str(self.arg3[i]))
                        self.instrSpaced.append(self.bin2StringSpacedIM(line))

                    elif (masked >= 1440) & (masked <= 1447):  # CBZ
                        # ---------read----------
                        self.opcode.append(masked>>3)
                        self.opcodeStr.append("CBZ")
                        self.arg1.append((int(line, 2) & rdMask))
                        self.arg2.append(self.readSignedBinNumberCBZ((int(line, 2) & addr2Mask) >> 5))
                        self.arg3.append(0)
                        self.opcodeSpace.append("\t")
                        self.arg1Str.append("\tR" + str(self.arg1[i]))
                        self.arg2Str.append(", #" + str(self.arg2[i]))
                        self.arg3Str.append("")
                        self.instrSpaced.append(self.bin2StringSpacedCB(line))

                    elif (masked >= 1448) & (masked <= 1455):  # CBNZ
                        # ---------read----------
                        self.opcode.append(masked>>3)
                        self.opcodeStr.append("CBNZ")
                        self.arg1.append((int(line, 2) & rdMask))
                        self.arg2.append(self.readSignedBinNumberCBZ((int(line, 2) & addr2Mask) >> 5))
                        self.arg3.append(0)
                        self.opcodeSpace.append("")
                        self.arg1Str.append("\tR" + str(self.arg1[i]))
                        self.arg2Str.append(", #" + str(self.arg2[i]))
                        self.arg3Str.append("")
                        self.instrSpaced.append(self.bin2StringSpacedCB(line))

                    elif (masked >= 160) & (masked <= 191):  # B
                        # ---------read----------
                        self.opcode.append(masked>>5)
                        self.opcodeStr.append("B")
                        self.arg1.append(long(self.readSignedBinNumberB(int(line, 2) & branchMask)))
                        self.arg2.append(0)
                        self.arg3.append(0)
                        self.opcodeSpace.append("\t")
                        self.arg1Str.append("\t#" + str(self.arg1[i]))
                        self.arg2Str.append("")
                        self.arg3Str.append("")
                        self.instrSpaced.append(self.bin2StringSpacedB(line))

                    elif (masked == 0):  # NOP
                        # ---------read----------
                        self.opcode.append(masked>>5)
                        self.opcodeStr.append("NOP")
                        self.arg1.append(0)
                        self.arg2.append(0)
                        self.arg3.append(0)
                        self.opcodeSpace.append("")
                        self.arg1Str.append("")
                        self.arg2Str.append("")
                        self.arg3Str.append("")
                        self.instrSpaced.append(self.bin2StringSpacedB(line))

                else:
                    # ---------read----------
                    extra= 0
                    if((int(line,2)>>31)==0x1):
                        extra = ((int(line,2)^0xFFFFFFFF)-0x1)*-1
                    else:
                        extra = int(line,2)
                    self.dataEnd = i
                    self.opcode.append(0)
                    self.opcodeStr.append(extra)
                    self.arg1.append(0)
                    self.arg2.append(0)
                    self.arg3.append(0)
                    self.opcodeSpace.append("")
                    self.arg1Str.append("")
                    self.arg2Str.append("")
                    self.arg3Str.append("")
                    self.instrSpaced.append(line[0:32]+"\t")

                # ----------memory---------
                #outFile.write('writting '+str(extra)+'to mem')
                self.mem.append(extra)
                self.binMem.append(line)
                # ----------print---------- (this gives errors as of right now, the errors will be fixed once the other functions are fixed)
                outFile.write(str(self.instrSpaced[i]) + "\t" + str(96+(i*4)) + "\t\t" + str(self.opcodeStr[i]) + self.opcodeSpace[i] + self.arg1Str[i] + self.arg2Str[i] + self.arg3Str[i]+"\n")
                i=i+1 #incriment i
                if 'str' in line:
                    break

    def bin2StringSpacedR(self, line):
        out = line[0:11]+" "+line[11:16]+" "+line[16:22]+" "+line[22:27]+" "+line[27:32]
        return out

    def bin2StringSpacedD(self, line):
        out = line[0:11]+" "+line[11:20]+" "+line[20:22]+" "+line[22:27]+" "+line[27:32]
        return out

    def bin2StringSpacedI(self, line):
        out = line[0:10]+" "+line[10:22]+" "+line[22:27]+" "+line[27:32]+"\t"
        return out

    def bin2StringSpacedIM(self, line):
        out = line[0:9]+" "+line[9:11]+" "+line[11:27]+" "+line[27:32]+"\t"
        return out

    def bin2StringSpacedCB(self, line):
        out = line[0:8]+" "+line[8:27]+" "+line[27:32]+"\t"
        return out

    def bin2StringSpacedB(self, line):
        out = line[0:6]+" "+line[6:32]+"\t"
        return out

    def bin2StringSpacedBreak(self, line):
        out = line[0:8]+" "+line[8:11]+" "+line[11:16]+" "+line[16:21]+" "+line[21:26]+" "+line[26:32]
        return out

    def readSignedBinNumberB(self, line):

        if(((line>>25)&0b1)==1):
            out = (0x3FFFFFF^(line-0b1))*-1
        else:
            out = line
        return out

    def readSignedBinNumberCBZ(self, line):

        if(((line>>18)&0b1)==1):
            out = (0x7FFFF^(line-0b1))*-1
        else:
            out = line
        return out


#---------------------------------arm sim----------------------------------
class ArmSim:
    preIssue = []
    preALU = Queue.Queue(maxsize=2)
    preMem = Queue.Queue(maxsize=2)
    postALU = [-1]*2 #position 1 is for location and 2 is for data
    postMem = [-1]*3 #third position is for indicating mem or register
    registers = [0] * 32
    PC = 0
    data = [0]
    broken = 0
    arm = ArmDecode()
    cycle = 1
    currentPC = 1

    def __init__(self):
        self.IF = IF()
        self.Issue_unit = Issue_unit()
        self.ALU = ALU()
        self.Mem = Mem()
        self.WB = WB()
        self.cache = []


    def run(self):
        while(self.broken == 0):
            self.WB.run()
            self.Mem.run()
            self.ALU.run()
            self.Issue_unit.run()
            self.IF.run()
            print('PC:')
            print(self.PC)
    def basic_run(self):
        
        self.arm.run()

        outputFileName2 = self.arm.outputFileName + '_sim.txt'
        outFile = open(outputFileName2, 'w')




        while (self.broken == 0):

            self.currentPC = self.PC

            if self.arm.opcodeStr[self.PC]=="ADD":  # ADD
                # -----perform operation------
                self.registers[self.arm.arg1[self.PC]] = self.registers[self.arm.arg2[self.PC]] + self.registers[self.arm.arg3[self.PC]]


            elif self.arm.opcodeStr[self.PC]=="SUB":  # SUB
                # -----perform operation------
                self.registers[self.arm.arg1[self.PC]] = self.registers[self.arm.arg2[self.PC]] - self.registers[self.arm.arg3[self.PC]]

            elif self.arm.opcodeStr[self.PC]=="LSL":  # LSL
                # -----perform operation------
                self.registers[self.arm.arg1[self.PC]]= self.registers[self.arm.arg2[self.PC]] % 0x100000000 << self.arm.arg3[self.PC]

            elif self.arm.opcodeStr[self.PC]=="LSR": # LSR
                # -----perform operation------
                self.registers[self.arm.arg1[self.PC]]= self.registers[self.arm.arg2[self.PC]] >> self.arm.arg3[self.PC]

            elif self.arm.opcodeStr[self.PC]=="ASR": # ASR
                # -----perform operation------
                if((self.registers[self.arm.arg2[self.PC]]>>4)==1):
                    temp = self.registers[self.arm.arg2[self.PC]]
                    for x in self.arm.arg3[self.PC]:
                        temp = (temp>>1)^0x10
                    self.registers[self.arm.arg1[self.PC]] = temp
                else:
                    self.registers[self.arm.arg1[self.PC]]= self.registers[self.arm.arg2[self.PC]] >> self.arm.arg3[self.PC]

            elif self.arm.opcodeStr[self.PC]=="AND":  # AND
                # -----perform operation------
                self.registers[self.arm.arg1[self.PC]] = self.registers[self.arm.arg2[self.PC]] & self.registers[self.arm.arg3[self.PC]]


            elif self.arm.opcodeStr[self.PC]=="ORR":  # ORR
                # -----perform operation------
                self.registers[self.arm.arg1[self.PC]] = self.registers[self.arm.arg2[self.PC]] | self.registers[self.arm.arg3[self.PC]]


            elif self.arm.opcodeStr[self.PC]=="EOR":  # EOR
                # -----perform operation------
                self.registers[self.arm.arg1[self.PC]] = self.registers[self.arm.arg2[self.PC]] ^ self.registers[self.arm.arg3[self.PC]]


            elif self.arm.opcodeStr[self.PC]=="BREAK":  # BREAK
                # -----perform operation------

                self.broken = 1

            elif self.arm.opcodeStr[self.PC]=="LDUR":  # LDUR
                # -----perform operation------
                try:
                    self.registers[self.arm.arg1[self.PC]] = self.arm.mem[(self.registers[self.arm.arg2[self.PC]]+(self.arm.arg3[self.PC]))/4+6]
                except:
                    self.registers[self.arm.arg1[self.PC]] = 0

            elif self.arm.opcodeStr[self.PC]=="STUR":  # STUR
                # -----perform operation------
                self.storeMem(((self.registers[self.arm.arg2[self.PC]] + (self.arm.arg3[self.PC]))/4)-2, self.registers[self.arm.arg1[self.PC]])

            elif self.arm.opcodeStr[self.PC]=="ADDI":  # ADDI
                # -----perform operation------
                self.registers[self.arm.arg1[self.PC]] = self.registers[self.arm.arg2[self.PC]] + self.arm.arg3[self.PC]


            elif self.arm.opcodeStr[self.PC]=="SUBI":  # SUBI
                # -----perform operation------
                self.registers[self.arm.arg1[self.PC]] = self.registers[self.arm.arg2[self.PC]] - self.arm.arg3[self.PC]

            elif self.arm.opcodeStr[self.PC]=="MOVZ":  # MOVZ
                # -----perform operation------
                self.registers[self.arm.arg1[self.PC]] = (self.arm.arg2[self.PC])<<(self.arm.arg3[self.PC])

            elif self.arm.opcodeStr[self.PC]=="MOVK":  # MOVK
                # -----perform operation------
                temp = (self.arm.arg2[self.PC])<<(self.arm.arg3[self.PC])
                self.registers[self.arm.arg1[self.PC]] = temp | self.registers[self.arm.arg1[self.PC]]

            elif self.arm.opcodeStr[self.PC]=="CBZ":  # CBZ
                # -----perform operation------
                if(self.registers[self.arm.arg1[self.PC]]==0):
                    self.PC=(self.PC+ self.arm.arg2[self.PC])-1

            elif self.arm.opcodeStr[self.PC]=="CBNZ":  # CBNZ
                # -----perform operation------
                if (self.registers[self.arm.arg1[self.PC]] != 0):
                    self.PC = self.PC+ self.arm.arg2[self.PC] - 1

            elif self.arm.opcodeStr[self.PC]=="B":  # B
                # -----perform operation------
                self.PC = (self.PC + self.arm.arg1[self.PC])-1

            elif self.arm.opcodeStr[self.PC]=="NOP":  # NOP
                # -----perform operation------
                broken=0


            #--------------------------output----------------------------
            outFile.write('=====================\n')
            outFile.write('cycle:'+str(self.cycle)+'\t'+str(self.currentPC*4+96))
            outFile.write('\t'+self.arm.opcodeStr[self.currentPC]+ self.arm.arg1Str[self.currentPC] + self.arm.arg2Str[self.currentPC] + self.arm.arg3Str[self.currentPC]+"\n\n")
            outFile.write('registers:\n')
            for x in range(4):
                outFile.write('r'+("%02d" % (x*8,))+':')
                for y in range(8):
                    outFile.write('\t'+str(self.registers[x*8+y]))
                outFile.write('\n')

            outFile.write('\ndata:\n')
            if(self.arm.dataEnd>self.arm.dataStart):
                outFile.write(str((self.arm.dataStart + 1) * 4 + 96)+':')
            else:
                outFile.write("\n")
            temp = 0
            for x in range(self.arm.dataEnd-self.arm.dataStart):
                if(temp == 8):
                    temp = 0
                    outFile.write('\n'+str((self.arm.dataStart + x + 1) * 4 + 96 ) + ':')
                outFile.write(str(self.arm.mem[x+1+self.arm.dataStart]))
                temp=temp+1
                if (temp != 8):
                    outFile.write('\t')
            if(self.broken == 0):
                outFile.write('\n')


            self.PC = self.PC + 1
            self.cycle = self.cycle + 1


    def storeMem(self, location, data):
        if(len(self.arm.mem)<location):
            i = 0
            location = location+8
            temp = len(self.arm.mem)%8
            for x in range(temp):
                self.arm.mem.append(0)
                self.arm.binMem.append(0)
            while(len(self.arm.mem)-1<location):#(i<=(((location-temp)+7)/8)*8): #round up to nearest multiple of 8
                for x in range(8):
                    self.arm.mem.append(0)
                    self.arm.binMem.append(0)
                i=i+8
            self.arm.dataEnd = self.arm.dataEnd+i
            self.arm.mem[location] = data
        else:
            self.arm.mem[location]=data


class IF:
    #def __init__(self):

    def run(self):
        if(4 >= len(ArmSim.preIssue)):
            ArmSim.preIssue.append(ArmSim.PC)
            ArmSim.PC=ArmSim.PC+1
        if (4 >= len(ArmSim.preIssue)):
            ArmSim.preIssue.append(ArmSim.PC)
            ArmSim.PC = ArmSim.PC + 1


class Issue_unit:

    def run(self):
        count = 0
        if(len(ArmSim.preIssue)>0):
            for i in ArmSim.preIssue:
                if(ArmDecode.opcodeStr[i] in ['LDUR' ,'STUR'] ):
                    if(ArmSim.preMem.full() != 1):
                        ArmSim.preMem.put(ArmSim.preIssue.pop(i))
                        count=count+1
                else:
                    if (ArmSim.preALU.full() != 1):
                        ArmSim.preALU.put(ArmSim.preIssue.pop(i))
                        count=count+1
                if(count == 2):
                    return
        else:
            print('howdy')


class ALU:

    def run(self):
        self.PC=ArmSim.preALU.get()

        if ArmDecode.opcodeStr[self.PC] == "ADD":  # ADD
            # -----perform operation------
            ArmSim.postALU[1] = ArmSim.registers[ArmDecode.arg2[self.PC]] + ArmSim.registers[
                ArmDecode.arg3[self.PC]]
            ArmSim.postALU[0] = ArmDecode.arg1[self.PC]


        elif ArmDecode.opcodeStr[self.PC] == "SUB":  # SUB
            # -----perform operation------
            ArmSim.postALU[1] = ArmSim.registers[ArmDecode.arg2[self.PC]] - ArmSim.registers[
                ArmDecode.arg3[self.PC]]
            ArmSim.postALU[0] = ArmDecode.arg1[self.PC]

        elif ArmDecode.opcodeStr[self.PC] == "LSL":  # LSL
            # -----perform operation------
            ArmSim.postALU[1] = ArmSim.registers[ArmDecode.arg2[self.PC]] % 0x100000000 << \
                                                     ArmDecode.arg3[self.PC]
            ArmSim.postALU[0] = ArmDecode.arg1[self.PC]

        elif ArmDecode.opcodeStr[self.PC] == "LSR":  # LSR
            # -----perform operation------
            ArmSim.postALU[1] = ArmSim.registers[ArmDecode.arg2[self.PC]] >> ArmDecode.arg3[self.PC]
            ArmSim.postALU[0] = ArmDecode.arg1[self.PC]

        elif ArmDecode.opcodeStr[self.PC] == "ASR":  # ASR
            # -----perform operation------
            if ((ArmSim.registers[ArmDecode.arg2[self.PC]] >> 4) == 1):
                temp = ArmSim.registers[ArmDecode.arg2[self.PC]]
                for x in ArmDecode.arg3[self.PC]:
                    temp = (temp >> 1) ^ 0x10
                ArmSim.postALU[1] = temp
            else:
                ArmSim.postALU[1] = ArmSim.registers[ArmDecode.arg2[self.PC]] >> ArmDecode.arg3[
                    self.PC]
            ArmSim.postALU[0] = ArmDecode.arg1[self.PC]

        elif ArmDecode.opcodeStr[self.PC] == "AND":  # AND
            # -----perform operation------
            ArmSim.postALU[1] = ArmSim.registers[ArmDecode.arg2[self.PC]] & ArmSim.registers[
                ArmDecode.arg3[self.PC]]
            ArmSim.postALU[0] = ArmDecode.arg1[self.PC]


        elif ArmDecode.opcodeStr[self.PC] == "ORR":  # ORR
            # -----perform operation------
            ArmSim.postALU[1] = ArmSim.registers[ArmDecode.arg2[self.PC]] | ArmSim.registers[
                ArmDecode.arg3[self.PC]]
            ArmSim.postALU[0] = ArmDecode.arg1[self.PC]


        elif ArmDecode.opcodeStr[self.PC] == "EOR":  # EOR
            # -----perform operation------
            ArmSim.postALU[1] = ArmSim.registers[ArmDecode.arg2[self.PC]] ^ ArmSim.registers[
                ArmDecode.arg3[self.PC]]
            ArmSim.postALU[0] = ArmDecode.arg1[self.PC]


        elif ArmDecode.opcodeStr[self.PC] == "BREAK":  # BREAK
            # -----perform operation------

            ArmSim.broken = 1

        elif ArmDecode.opcodeStr[self.PC] == "ADDI":  # ADDI
            # -----perform operation------
            ArmSim.postALU[1] = ArmSim.registers[ArmDecode.arg2[self.PC]] + ArmDecode.arg3[self.PC]
            ArmSim.postALU[0] = ArmDecode.arg1[self.PC]


        elif ArmDecode.opcodeStr[self.PC] == "SUBI":  # SUBI
            # -----perform operation------
            ArmSim.postALU[1] = ArmSim.registers[ArmDecode.arg2[self.PC]] - ArmDecode.arg3[self.PC]
            ArmSim.postALU[0] = ArmDecode.arg1[self.PC]

        elif ArmDecode.opcodeStr[self.PC] == "MOVZ":  # MOVZ
            # -----perform operation------
            ArmSim.postALU[1] = (ArmDecode.arg2[self.PC]) << (ArmDecode.arg3[self.PC])
            ArmSim.postALU[0] = ArmDecode.arg1[self.PC]

        elif ArmDecode.opcodeStr[self.PC] == "MOVK":  # MOVK
            # -----perform operation------
            temp = (ArmDecode.arg2[self.PC]) << (ArmDecode.arg3[self.PC])
            ArmSim.postALU[1] = temp | ArmSim.postALU[1]
            ArmSim.postALU[0] = ArmDecode.arg1[self.PC]

        elif ArmDecode.opcodeStr[self.PC] == "CBZ":  # CBZ
            # -----perform operation------
            if (ArmSim.registers[ArmDecode.arg1[self.PC]] == 0):
                self.PC = (self.PC + ArmDecode.arg2[self.PC]) - 1

        elif ArmDecode.opcodeStr[self.PC] == "CBNZ":  # CBNZ
            # -----perform operation------
            if (ArmSim.registers[ArmDecode.arg1[self.PC]] != 0):
                self.PC = self.PC + ArmDecode.arg2[self.PC] - 1

        elif ArmDecode.opcodeStr[self.PC] == "B":  # B
            # -----perform operation------
            self.PC = (self.PC + ArmDecode.arg1[self.PC]) - 1

        elif ArmDecode.opcodeStr[self.PC] == "NOP":  # NOP
            # -----perform operation------
            broken = 0

class Mem:

    def run(self):
        self.PC = ArmSim.preMem.get()

        if ArmDecode.opcodeStr[self.PC] == "LDUR":  # LDUR
            # -----perform operation------
            try:
                ArmSim.postMem[1] = ArmDecode.mem[
                    (self.registers[ArmDecode.arg2[self.PC]] + (ArmDecode.arg3[self.PC])) / 4 + 6]
                ArmSim.postMem[0] = ArmDecode.arg1[self.PC]
            except:
                ArmSim.postMem[1] = 0
                ArmSim.postMem[0] = ArmDecode.arg1[self.PC]
                ArmSim.postMem[2] = 1

        elif ArmDecode.opcodeStr[self.PC] == "STUR":  # STUR
            # -----perform operation------
            ArmSim.postMem[1] = ((ArmSim.registers[ArmDecode.arg2[self.PC]] + (ArmDecode.arg3[self.PC])) / 4) - 2
            ArmSim.postMem[0] = ArmSim.registers[ArmDecode.arg1[self.PC]]
            ArmSim.postMem[2] = 2


class WB:
    def __init__(self):
        self.temp = 1

    def run(self):
        if(ArmSim.postMem[2]==2):
            ArmSim.storeMem(ArmSim.postMem[1],ArmSim.postMem[0])
        elif(ArmSim.postMem[2]==1):
            ArmSim.registers[ArmSim.postMem[0]] = ArmSim.postMem[1]

        if(ArmSim.postALU[0] != -1):
            ArmSim.registers[ArmSim.postALU[0]]= ArmSim.postALU[1]

        ArmSim.postALU = [-1]*2
        ArmSim.postMem = [-1]*3

class cacheBlock:
    def __init__(self):
        LRU=0

        valid1=0
        dirty1=0
        tag1=0
        data1=0

        valid2=0
        dirty2=0
        tag2=0
        data2=0

def main():

    decode = ArmDecode()
    decode.run()
    sim = ArmSim()
    sim.basic_run()


if __name__ == "__main__":
    main()
