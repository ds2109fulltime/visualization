def maps(latitude = 40.4167 , longitude = -3.70325, zoom = 6):
    '''This function displays a map based on the latitude, longitude, and zoom.
    By default it will show Spain'''

    import folium
    from IPython.display import display
    
    center = [latitude, longitude]
    my_map = folium.Map(location=center, zoom_start=zoom)
    display(my_map)
