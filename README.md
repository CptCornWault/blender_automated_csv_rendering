<style type="text/css">
    ol {
        list-style-type: lower-alpha;
    }
</style>

# blender_automated_csv_rendering v1.x
A lesson in automating renders from a CSV file in blender<br />
This lesson and its instructions is a work in progress, but feel free to use it any time.<br />
Check back later for links to the youtube video series.<br />
If you encounter a problem with the instructions or the script, please don't hesitate to file an issue.

## Step 1
Clone this repository into your blender project.
```
cd ~/path/to/my/project
git clone https://github.com/CptCornWault/blender_automated_csv_rendering.git
```

## Step 2
Setup the project path.<br />

 Open `blender_automated_csv_rendering/lessons/csv_render_1.py` and replace the `projectPath` with the full system path to your project.<br />

 For for these lessons, include `automated_csv_rendering\\lessons\\` in your path so that the script will know where to find the jobs, textures, and renders related to these lessons.
 ```
projectPath = 'C:\\path\\to\\my\\project\\automated_csv_rendering\\lessons\\'
 ```
 Don't forget to escape the slashes (`\\`) and use the trailing slash.

 ## Step 3
 Setup the lesson<br />

 In teh same file as step two, update the `currentJobFilePath` with the path to the lesson directory you want to work from.<br />

Lesson 1 is set by default
 ```
currentJobFilePath = projectPath + 'lesson_1\\'
 ```

 ## Step 3
 Begin lesson 1

  1. Open Blender (For this tutorial we are using blender v2.82a for Windows) and set up a default scene with the default cube. If you are using an older vesion ov Blender you may have to UV unwrap the Cube.
  
  2. Make sure the cube object is named `Cube`. If you want to use a different name, make sure the `objectName` reflects your object name.
      ```
      objectName = "Cube"
      ```

  3. Apply a material to your object, and name the material `cube_mat`. You can use a different name for the material if you change the `material_slots` key that is being accessed to define the `material` variable.
      ```
      material = renderObject.material_slots['cube_mat'].material
      ```

  4. Set up the material to use an image texture.

  5. Open the scripting panel and load `/lessons/lesson_1/csv_render_lesson_1.py`. Also open the System Console so that you can see the script output.

  6. Run the script. It will output progress and tell you when it is finished. If there is a problem, plender will tell you the error message and where it occured.