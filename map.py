import folium

#create map
m = folium.Map(location=[-22.4659781, 23.6591281], zoom_start=7)

#quarantine tooltip
qtooltip = 'Quarantine center'

#custom marker icon
logoIcon = folium.features.CustomIcon('quarantine.png', icon_size=(20,20))
logoIcond = folium.features.CustomIcon('quarantine.png', icon_size=(20,20))

#quarantine marker
folium.Marker([-20.0342842, 23.4292139], popup = ' <div class="thumbnail" style="width:300px"> <img src="https://oncologynews.com.au/wp-content/uploads/University_of_Botswana_Teaching_Hospital_Gaborone-e1554096965327.jpg" alt="image"> <div class="caption"> <h3>Matshwane Clinic</h3> <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint est error necessitatibus fugiat iusto, Natus pariatur quibusdam harum hic unde ad illo cupiditate vel, eius repellendus possimus odio minus culpa. Saepe!</p> <p><a href="#" class="btn btn-primary" role="button">Call</a> <a href="#" class="btn btn-default" role="button">Button</a></p> </div> </div> ', tooltip = qtooltip, icon=logoIcon).add_to(m),
folium.Marker([-24.650994, 25.9467775],
            popup = ' <div class="thumbnail" style="width:300px"> <img src="https://oncologynews.com.au/wp-content/uploads/University_of_Botswana_Teaching_Hospital_Gaborone-e1554096965327.jpg" alt="image"> <div class="caption"> <h3>Sir Ketumile Masire Practice Hospital</h3> <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint est error necessitatibus fugiat iusto, aliquam excepturi dolores, doloribus laboriosam facere explicabo nam atque quibusdam totam, at libero. Quam, ab qui!Nostrum laborum esse amet, nesciunt quia voluptates. Natus pariatur quibusdam harum hic unde ad illo cupiditate vel, eius repellendus possimus odio minus culpa. Saepe!</p> <p><a href="#" class="btn btn-primary" role="button">Call</a> <a href="#" class="btn btn-default" role="button">Button</a></p> </div> </div> ',
            tooltip = qtooltip,
            icon=logoIcond).add_to(m),





#generate map
m.save('map.html')