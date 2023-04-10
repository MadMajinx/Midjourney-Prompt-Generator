import openai
import streamlit as st

styles=["action painting","Aerial perspective","Airbrush painting","Allegory","Analogous colors","Assemblage","Baroque painting","Body painting","Calligraphy","Cameo","Chiaroscuro","Color field painting","Color theory","Comic book art","Constructivism","Cubism","Cultural arts","Dadaism","Decoupage","Digital art","Encaustic painting","Environmental art","Etching","Expressionism","Fauvism","Fiber arts","Fresco painting","Geometric abstraction","Glassblowing","Graffiti art","Grisaille","Hard-edge painting","Iconography","Impressionism","Installation art","Jewelry design","Kinetic art","Landscape painting","Lyrical abstraction","Manga art","Marbling","Minimalism","Mixed media","Mosaic","Naive art","Neo-classicism","Op art","Ornamentation","Paper craft","Papier-mache","Pastel painting","Performance art","Photo realism","Pointillism","Pop art","Portrait painting","Poster design","Printmaking","Realism","Relief sculpture","Rococo","Romanesque art","Sculpture","Silkscreen printing","Surrealism","Symbolism","Tapestry","Tenebrism","Textile art","Trompe-l'oeil","Urban art","Vanitas","Vernacular architecture","Video art","Vitreography","Watercolor painting","Wearable art","Wire sculpture","Wood carving","Woodcut","Xylography","Zentangle art","Zen art","3D printing","Ceramics","Choreography","Collage","Digital painting","Film","Metalworking","Musical composition","Narrative art","Photography","Sculpture","Silversmithing","Typography","Videography","Visual storytelling","Weaving","Writing","Yarn bombing","Body casting","Camera obscura","Casting","Cathedral architecture","Ceramic art","Ceramic glaze","Chasing","Cloisonne","Cold-working","Computer-generated art","Conceptual art","Crosshatching","Diorama","Found object art","Land art","Low-relief sculpture","Performance sculpture"]
lightings=[  "Cinematic Lighting" , "Natural lighting",    "Ambient lighting",    "Overhead lighting",    "Softbox lighting",    "Ring light",    "Fresnel light",    "LED lighting",    "Strobe lighting",    "Spotlight",    "Backlighting",    "Rim lighting",    "Side lighting",    "Fill lighting",    "High key lighting",    "Low key lighting",    "Chiaroscuro lighting",    "Rembrandt lighting",    "Butterfly lighting",    "Broad lighting",    "Short lighting",    "Split lighting",    "Strip lighting",    "Top lighting",    "Bottom lighting",    "Up-lighting",    "Down-lighting",    "Cross-lighting",    "Bounce lighting",    "Diffused lighting",    "Hard lighting",    "Soft lighting",    "Colored lighting",    "Directional lighting",    "Omnidirectional lighting",    "Selective lighting",    "Accent lighting",    "Mood lighting",    "Task lighting",    "Under-cabinet lighting",    "Display lighting"]
cameras=["Wide-angle lens", "Telephoto lens", "Fish-eye lens", "Tilt-shift lens", "Macro lens", "Prime lens", "Zoom lens", "Lensbaby lens", "Large format camera", "Medium format camera", "Polaroid camera", "Pinhole camera", "Holga camera", "Lomography camera", "Toy camera", "View camera", "SLR camera", "Rangefinder camera", "Mirrorless camera", "Full-frame camera", "APS-C camera", "35mm film camera", "Large format film camera", "Instant film camera", "Digital single-lens reflex (DSLR) camera", "Compact camera", "Camcorder", "GoPro camera", "Point-and-shoot camera", "Mirrorless interchangeable-lens camera (MILC)"]
artists=["Leonardo da Vinci", "Michelangelo", "Rembrandt", "Vincent van Gogh", "Claude Monet", "Pablo Picasso", "Salvador Dali", "Wassily Kandinsky", "Georgia O'Keeffe", "Jackson Pollock", "Mark Rothko", "Willem de Kooning", "Francis Bacon", "Roy Lichtenstein", "Andy Warhol", "Keith Haring", "Jean-Michel Basquiat", "Frida Kahlo", "Diego Rivera", "Edvard Munch", "Gustav Klimt", "Egon Schiele", "Paul Cézanne", "Henri Matisse", "Piet Mondrian", "Kazimir Malevich", "Edward Hopper", "Grant Wood", "René Magritte", "Max Ernst", "Joan Miró", "Marc Chagall", "Henri Cartier-Bresson", "Ansel Adams", "Cindy Sherman", "Jeff Koons", "Damien Hirst", "Yayoi Kusama", "Ai Weiwei", "Banksy"]
colors= ['White', 'Black', 'Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Pink', 'Orange', 'Brown', 'Gray', 'Silver', 'Gold', 'Bronze', 'Magenta', 'Turquoise', 'Maroon', 'Olive', 'Navy', 'Teal', 'Lavender', 'Beige', 'Cream', 'Khaki', 'Fuchsia', 'Salmon', 'Sky blue', 'Peach', 'Sienna', 'Indigo', 'Mustard', 'Rust', 'Coral', 'Chartreuse', 'Burnt sienna', 'Periwinkle', 'Crimson', 'Electric blue', 'Mauve', 'Brick red', 'Jade', 'Saffron', 'Eggplant', 'Vermilion', 'Honeydew', 'Cerulean', 'Amethyst', 'Tangerine', 'Slate gray', 'Forest green']
materials=['Paper', 'Canvas', 'Wood', 'Metal', 'Clay', 'Stone', 'Glass', 'Fabric', 'Leather', 'Plastic',              'Resin', 'Wax', 'Ink', 'Charcoal', 'Graphite', 'Watercolor', 'Oil paint', 'Acrylic paint', 'Pastels',              'Colored pencils', 'Chalk', 'Pigments', 'Gold leaf', 'Silver leaf', 'Copper leaf', 'Bronze', 'Brass',              'Steel', 'Aluminum', 'Bronze powder', 'Plaster', 'Cement', 'Sand', 'Soil', 'Moss', 'Ice', 'Feathers',              'Fur', 'Hair', 'Bones', 'Shells', 'Seeds', 'Flowers', 'Fruits', 'Vegetables', 'Tea bags', 'Coffee grounds',              'Sawdust', 'Cork', 'Rubber']
qualitys=['hyperrealistic','realistic','8K','4K','2K','Low resolution', 'High resolution', 'Grainy', 'Pixelated', 'Blurry', 'Sharp', 'Overexposed', 'Underexposed', 'Contrast', 'Saturation', 'Brightness', 'Noise', 'Distortion', 'Clarity', 'Dynamic range', 'Color accuracy', 'Depth of field', 'Bokeh', 'Artifacts', 'Compression']



st.title('Midjourney Prompt Generator')
content=st.text_input('Enter your subject/scene:')
content_check=st.checkbox('Generate randomly')
temperature=st.slider('Select the temperature for the prompt:',min_value=0.0,max_value=2.0,)

st.subheader('Select the different attributes for the prompt')
col1,col2=st.columns(2)

with col1:
     style=st.selectbox('Style',styles)
     style_check=st.checkbox('Include style')
     lighting=st.selectbox('Lighting',lightings)
     lighting_check=st.checkbox('Include lighting')
     camera=st.selectbox('Camera/Lens',cameras)
     camera_check=st.checkbox('Include camera/lens')
     artist=st.selectbox('Artist',artists)
     artist_check=st.checkbox('Include artist')
    
with col2:
     color=st.selectbox('Color',colors)
     color_check=st.checkbox('Include color')
     material=st.selectbox('Material',materials)
     material_check=st.checkbox('Include material')
     quality=st.selectbox('Quality',qualitys)
     quality_check=st.checkbox('Include quality')
     misc=st.text_input('Miscellaneous:')
     misc_check=st.checkbox('Include miscellaneous:')

exclude=st.text_input('If you want to exclude any ideas from the prompt, enter below:')

prompt_list=[]

if style_check:
     prompt_list.append(style)

if lighting_check:
     prompt_list.append(lighting)

if camera_check:
     prompt_list.append(camera)

if artist_check:
     prompt_list.append(f'inspired by {artist}')

if color_check:
     prompt_list.append(color)

if material_check:
     prompt_list.append(material)

if quality_check:
     prompt_list.append(quality)

if misc_check:
     prompt_list.append(misc)

prompt_list = ','.join(prompt_list)

openai.api_key = "[OpemAI API Key]" # or use the method we defined earlier

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=temperature,
    )
    return response.choices[0].text.strip()

def prompt_generator(chatgpt_prompt):

    if exclude=="":
        
        prompt1 = f"create a hypothetical creative scene with the following: {chatgpt_prompt} "
        response1 = generate_response(prompt1)
    else:
        
        prompt1 = f"create a hypothetical creative scene with the following: {chatgpt_prompt}. Also avoid the following ideas in the prompt: {exclude}  "
        response1 = generate_response(prompt1)

    prompt2 = f'Summarize the following text to a maximum of 30 words. Remove punctuations wherever possible.Focus on keeping keywords so that the essence of the text is maintained: {response1}'
    response2 = generate_response(prompt2)

    return response2

if st.button('Generate'):
     
    if content_check:
        
        prompt3="Generate a random subject/event for a story"
        response3=generate_response(prompt3)
        output=prompt_generator(prompt3)

    else:
        
        output=prompt_generator(content)

    output2= output + prompt_list
    st.text(f'{output2}')
