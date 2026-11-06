status=[0,0]
status[0]="dirty"
status[1]="dirty"
current_pos="A"
pos=0;
print("The Starting Point is A ")
while(status[0]=="dirty" or status[1]=="dirty"):
  print(f"{current_pos} is dirty")
  if(status[pos]=="dirty"):
    print(f"{current_pos} is getting cleaned");
    status[pos]="clean"
  if(current_pos=="A"):
    print("Move Right to B")
    current_pos="B"
    pos=1
  else:
    current_pos="A"
    pos=0

print(f"both rooms A and B are {status}")
