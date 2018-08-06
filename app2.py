import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

a = [1,3,7]
b = [2,4,6]

app.layout = html.Div(children=[
   html.H1(children="hello Dash"),
    
   html.Div(children='''
   Dash: A Web Application framework for Python
   '''),

   dcc.Graph(
   id='example-graph',
   figure={
     'data': [
      {'x': a, 'y': b, 'type': 'line', 'name': 'a-b'},
      {'x': b, 'y': a, 'type': 'line', 'name': 'b-a'}		
     ],
     'layout':{
         'title': 'Dash Data Visualization'
     }
  } 
)

])

if __name__ == '__main__':
    app.run_server(debug=True)
