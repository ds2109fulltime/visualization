def maps(latitude = 40.4167 , longitude = -3.70325, zoom = 6):
    '''Esta función muestra un mapa en función de la latitud, longitud y zoom introducidos.
    Por defecto mostrará España'''

    import folium
    from IPython.display import display
    
    center = [ latitude, longitude]
    my_map = folium.Map(location=center, zoom_start=zoom)
    display(my_map)