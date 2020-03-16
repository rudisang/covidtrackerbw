import folium

#create map
m = folium.Map(location=[-22.4659781, 23.6591281], zoom_start=7)

#quarantine tooltip
qtooltip = 'Quarantine center'

#custom marker icon
logoIcon = folium.features.CustomIcon('quarantine.png', icon_size=(20,20))
logoIcond = folium.features.CustomIcon('quarantine.png', icon_size=(20,20))
logoIcone = folium.features.CustomIcon('quarantine.png', icon_size=(20,20))
logoIconf = folium.features.CustomIcon('quarantine.png', icon_size=(20,20))
logoIcong = folium.features.CustomIcon('quarantine.png', icon_size=(20,20))
logoIconh = folium.features.CustomIcon('quarantine.png', icon_size=(20,20))
logoIconi = folium.features.CustomIcon('quarantine.png', icon_size=(20,20))
logoIconj = folium.features.CustomIcon('quarantine.png', icon_size=(20,20))
logoIconk = folium.features.CustomIcon('quarantine.png', icon_size=(20,20))

#quarantine marker
folium.Marker([-20.0342842, 23.4292139], popup = ' <div class="thumbnail" style="width:300px"> <img src="https://oncologynews.com.au/wp-content/uploads/University_of_Botswana_Teaching_Hospital_Gaborone-e1554096965327.jpg" alt="image"> <div class="caption"> <h3>Matshwane Clinic</h3> <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint est error necessitatibus fugiat iusto, Natus pariatur quibusdam harum hic unde ad illo cupiditate vel, eius repellendus possimus odio minus culpa. Saepe!</p> <p><a href="#" class="btn btn-primary" role="button">Call</a> <a href="#" class="btn btn-default" role="button">Button</a></p> </div> </div> ', tooltip = qtooltip, icon=logoIcon).add_to(m),
folium.Marker([-24.650994, 25.9467775],
            popup = ' <div class="thumbnail" style="width:300px"> <img src="https://oncologynews.com.au/wp-content/uploads/University_of_Botswana_Teaching_Hospital_Gaborone-e1554096965327.jpg" alt="image"> <div class="caption"> <h3>Sir Ketumile Masire Practice Hospital</h3> <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint est error necessitatibus fugiat iusto, aliquam excepturi dolores, doloribus laboriosam facere explicabo nam atque quibusdam totam, at libero. Quam, ab qui!Nostrum laborum esse amet, nesciunt quia voluptates. Natus pariatur quibusdam harum hic unde ad illo cupiditate vel, eius repellendus possimus odio minus culpa. Saepe!</p> <p><a href="#" class="btn btn-primary" role="button">Call</a> <a href="#" class="btn btn-default" role="button">Button</a></p> </div> </div> ',
            tooltip = qtooltip,
            icon=logoIcond).add_to(m),
folium.Marker([-19.6867824, 22.6621262],
            popup = ' <div class="thumbnail" style="width:300px"> <img src="https://oncologynews.com.au/wp-content/uploads/University_of_Botswana_Teaching_Hospital_Gaborone-e1554096965327.jpg" alt="image"> <div class="caption"> <h3>Kasane Hospital</h3> <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint est error necessitatibus fugiat iusto, aliquam excepturi dolores, doloribus laboriosam facere explicabo nam atque quibusdam totam, at libero. Quam, ab qui!Nostrum laborum esse amet, nesciunt quia voluptates. Natus pariatur quibusdam harum hic unde ad illo cupiditate vel, eius repellendus possimus odio minus culpa. Saepe!</p> <p><a href="#" class="btn btn-primary" role="button">Call</a> <a href="#" class="btn btn-default" role="button">Button</a></p> </div> </div> ',
            tooltip = qtooltip,
            icon=logoIcone).add_to(m),
folium.Marker([-21.1673776, 27.4719545],
            popup = ' <div class="thumbnail" style="width:300px"> <img src="https://oncologynews.com.au/wp-content/uploads/University_of_Botswana_Teaching_Hospital_Gaborone-e1554096965327.jpg" alt="image"> <div class="caption"> <h3>Ntshe Clinic</h3> <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint est error necessitatibus fugiat iusto, aliquam excepturi dolores, doloribus laboriosam facere explicabo nam atque quibusdam totam, at libero. Quam, ab qui!Nostrum laborum esse amet, nesciunt quia voluptates. Natus pariatur quibusdam harum hic unde ad illo cupiditate vel, eius repellendus possimus odio minus culpa. Saepe!</p> <p><a href="#" class="btn btn-primary" role="button">Call</a> <a href="#" class="btn btn-default" role="button">Button</a></p> </div> </div> ',
            tooltip = qtooltip,
            icon=logoIconf).add_to(m),
folium.Marker([-22.4190298, 21.5363381],
            popup = ' <div class="thumbnail" style="width:300px"> <img src="https://oncologynews.com.au/wp-content/uploads/University_of_Botswana_Teaching_Hospital_Gaborone-e1554096965327.jpg" alt="image"> <div class="caption"> <h3>Ghanzi Hospice</h3> <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint est error necessitatibus fugiat iusto, aliquam excepturi dolores, doloribus laboriosam facere explicabo nam atque quibusdam totam, at libero. Quam, ab qui!Nostrum laborum esse amet, nesciunt quia voluptates. Natus pariatur quibusdam harum hic unde ad illo cupiditate vel, eius repellendus possimus odio minus culpa. Saepe!</p> <p><a href="#" class="btn btn-primary" role="button">Call</a> <a href="#" class="btn btn-default" role="button">Button</a></p> </div> </div> ',
            tooltip = qtooltip,
            icon=logoIcong).add_to(m),
folium.Marker([-24.996784, 25.4781655],
            popup = ' <div class="thumbnail" style="width:300px"> <img src="https://oncologynews.com.au/wp-content/uploads/University_of_Botswana_Teaching_Hospital_Gaborone-e1554096965327.jpg" alt="image"> <div class="caption"> <h3>Peleng East Clinic</h3> <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint est error necessitatibus fugiat iusto, aliquam excepturi dolores, doloribus laboriosam facere explicabo nam atque quibusdam totam, at libero. Quam, ab qui!Nostrum laborum esse amet, nesciunt quia voluptates. Natus pariatur quibusdam harum hic unde ad illo cupiditate vel, eius repellendus possimus odio minus culpa. Saepe!</p> <p><a href="#" class="btn btn-primary" role="button">Call</a> <a href="#" class="btn btn-default" role="button">Button</a></p> </div> </div> ',
            tooltip = qtooltip,
            icon=logoIconh).add_to(m),
folium.Marker([-22.5593947, 27.1036604],
            popup = ' <div class="thumbnail" style="width:300px"> <img src="https://oncologynews.com.au/wp-content/uploads/University_of_Botswana_Teaching_Hospital_Gaborone-e1554096965327.jpg" alt="image"> <div class="caption"> <h3>Extension 11 Clinic</h3> <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint est error necessitatibus fugiat iusto, aliquam excepturi dolores, doloribus laboriosam facere explicabo nam atque quibusdam totam, at libero. Quam, ab qui!Nostrum laborum esse amet, nesciunt quia voluptates. Natus pariatur quibusdam harum hic unde ad illo cupiditate vel, eius repellendus possimus odio minus culpa. Saepe!</p> <p><a href="#" class="btn btn-primary" role="button">Call</a> <a href="#" class="btn btn-default" role="button">Button</a></p> </div> </div> ',
            tooltip = qtooltip,
            icon=logoIconi).add_to(m),
folium.Marker([-22.2800494, 20.0241662],
            popup = ' <div class="thumbnail" style="width:300px"> <img src="https://oncologynews.com.au/wp-content/uploads/University_of_Botswana_Teaching_Hospital_Gaborone-e1554096965327.jpg" alt="image"> <div class="caption"> <h3>Mamuno Boarder Clinic</h3> <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint est error necessitatibus fugiat iusto, aliquam excepturi dolores, doloribus laboriosam facere explicabo nam atque quibusdam totam, at libero. Quam, ab qui!Nostrum laborum esse amet, nesciunt quia voluptates. Natus pariatur quibusdam harum hic unde ad illo cupiditate vel, eius repellendus possimus odio minus culpa. Saepe!</p> <p><a href="#" class="btn btn-primary" role="button">Call</a> <a href="#" class="btn btn-default" role="button">Button</a></p> </div> </div> ',
            tooltip = qtooltip,
            icon=logoIconj).add_to(m),
folium.Marker([-19.3705808, 22.1672766],
            popup = ' <div class="thumbnail" style="width:300px"> <img src="https://oncologynews.com.au/wp-content/uploads/University_of_Botswana_Teaching_Hospital_Gaborone-e1554096965327.jpg" alt="image"> <div class="caption"> <h3>Gumare primary hostpital</h3> <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint est error necessitatibus fugiat iusto, aliquam excepturi dolores, doloribus laboriosam facere explicabo nam atque quibusdam totam, at libero. Quam, ab qui!Nostrum laborum esse amet, nesciunt quia voluptates. Natus pariatur quibusdam harum hic unde ad illo cupiditate vel, eius repellendus possimus odio minus culpa. Saepe!</p> <p><a href="#" class="btn btn-primary" role="button">Call</a> <a href="#" class="btn btn-default" role="button">Button</a></p> </div> </div> ',
            tooltip = qtooltip,
            icon=logoIconk).add_to(m),
            
            


# Circle marker
folium.CircleMarker(
    location=[-22.404735, 26.652829],
    radius=20,
    popup='<div class="alert alert-warning" role="alert">Low Risk zone! Proceed with caution. </div> <table class="table"> <thead> <tr> <th scope="col">Suspected</th> <th scope="col">Confirmed</th> <th scope="col">Recovered</th> <th scope="col">Infected</th> </tr> </thead> <tbody> <tr> <th scope="row">2</th> <td>2</td> <td>0</td> <td>1</td> </tr> </tbody> </table>',
    color='#FFFF00',
    fill=True,
    tooltip = 'Corona Zone',
    fill_color='#FFFF00'
).add_to(m)

folium.CircleMarker(
    location=[-19.2891378, 24.0796265],
    radius=20,
    popup='<div class="alert alert-danger" role="alert"> Warning! High infection zone. </div><table class="table"> <thead> <tr> <th scope="col">Suspected</th> <th scope="col">Confirmed</th> <th scope="col">Recovered</th> <th scope="col">Infected</th> </tr> </thead> <tbody> <tr> <th scope="row">5</th> <td>34</td> <td>3</td> <td>34</td> </tr> </tbody> </table>',
    color='#FF0000',
    fill=True,
    fill_color='#FF0000'
).add_to(m)

folium.CircleMarker(
    location=[-25.1335118, 24.9747709],
    radius=20,
    popup='<div class="alert alert-success" role="alert"> On the look Out. </div><table class="table"> <thead> <tr> <th scope="col">Suspected</th> <th scope="col">Confirmed</th> <th scope="col">Recovered</th> <th scope="col">Infected</th> </tr> </thead> <tbody> <tr> <th scope="row">5</th> <td>0</td> <td>0</td> <td>0</td> </tr> </tbody> </table>',
    color='#00FF00',
    fill=True,
    fill_color='#00FF00'
).add_to(m)





#generate map
m.save('map.html')