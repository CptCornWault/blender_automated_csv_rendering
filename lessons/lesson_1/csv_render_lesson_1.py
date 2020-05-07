import bpy,os,csv
print("#########################################################")
print("Render System Initializing...")

# Sets tha paths to the textures, jobs, and completed render directory.
projectPath = 'C:\\blender_experiments\\automated_csv_rendering\\lessons\\'
textureBasepath = projectPath + 'textures\\'
renderBasepath = projectPath + 'renders\\'
currentJobFilePath = projectPath + 'lesson_1\\'
print("Configuration Settings Loaded")

# Gets a list of the jobs and loads the first one to an array
renderJobsInDirectory = []
for file in os.listdir(currentJobFilePath):
    fileName, fileExtension = os.path.splitext(file)
    if fileExtension == '.csv':
        renderJobsInDirectory.append(file)
currentJobFilename = renderJobsInDirectory[0] #This will fail if there isn't a .csv file
print("Render Job Found")

# Opens the render job and loads each render to an array
renderJobCSV = open(currentJobFilePath+currentJobFilename, newline='')
renderJobReader = csv.reader(renderJobCSV, delimiter=',')
renderJob = []
for render in renderJobReader:
    renderJob.append(render)
renderJobCSV.close()
print("Render Job Imported")

# Loop through the renders in the job and execute the render routine
count = 1
print("Render Prosess Started")
for render in renderJob:
    print("---------------------- " + str(count))
    # Select the object
    objectName = "Cube"
    renderObject = bpy.data.objects[objectName]
    print("Selected " + objectName)

    # Select the material           
    material = renderObject.material_slots['cube_mat'].material    
    
    # Load the texture image
    textureImageName = render[0]
    textureImagePath = os.path.expanduser(textureBasepath + textureImageName)
    textureImage = bpy.data.images.load(textureImagePath)
    print("Texture Image Loaded")

    # Set the texture image        
    texture = material.node_tree.nodes['Image Texture']
    texture.image = textureImage
    print('Applied Image Texture')
    
    # Start the render
    print("Rendering...")
    scene = bpy.data.scenes['Scene']
    scene.render.filepath = renderBasepath + render[0] + ".jpg"
    bpy.ops.render.render( write_still=True )
    print("Render " + str(count) + " Saved")
     
    count += 1

print("#########################################################")
print("Done with " + (str(count-1)) + " render(s)!")
print("The render job is finished.")