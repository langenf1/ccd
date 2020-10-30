from ccd import Segment, CCD

if __name__ == '__main__':
    # Create segments
    seg1 = Segment(20, 0)
    seg2 = Segment(13, 0, seg1)
    seg3 = Segment(5, 0, seg2)

    segs = [seg1, seg2, seg3]

    # Create CCD and initialize arm
    ccd = CCD(segs)
    ccd.update_arm()

    # Move arm to target coordinates and plot the arm using matplotlib
    target = [25, 15, 0]
    ccd.move_to(target)
    ccd.plot_arm()

    # Additional information
    print(f"Error to target: {ccd.err_to_target}")
    for i in range(len(ccd.segments)):
        print(f"Segment {i+1} endpoint location: {ccd.segments[i].get_endpoint_location()}")
