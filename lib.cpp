#include "librealsense2/rs.hpp"   
#include "headers/header.h"

extern "C" float ** getDepth()
{
    rs2::pipeline p;

    p.start();

    rs2::frameset frames = p.wait_for_frames();

    rs2::depth_frame depth = frames.get_depth_frame();

    int width = (int) depth.get_width();
    int height = (int) depth.get_height();

    float **arr = new float*[height];
    for (int i = 0; i < height; i++)
    {
        arr[i] = new float[width];

        for (int j = 0; j < width; j++)
        {
            arr[i][j] = depth.get_distance(j, i);
        }
    }

    return arr;
}

extern "C" int * getDepthShape()
{
    rs2::pipeline p;

    p.start();

    rs2::frameset frames = p.wait_for_frames();

    rs2::depth_frame depth = frames.get_depth_frame();

    int *arr = new int[2];
    arr[0] = (int) depth.get_height();
    arr[1] = (int) depth.get_width();

    return arr;
}
