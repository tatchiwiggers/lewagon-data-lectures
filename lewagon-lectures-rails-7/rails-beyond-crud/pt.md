# BEYOND CRUD
ontem vcs viram então o CRUD em rails, hoje nos vamos falar de como ir alem de CRUD, como por exemplo vou mostrar pra vcs que nos nao estamos limitaos aos 7 CRUD actions, podemos criar rotas customizadas, vou mostrar pra vcs como criar rotar aninhadas e vamos falar tb de uma ferramenta de rails chamada scaffold.

# SETUP

# CREATE A NEW RAILS APP

# ADD BOOTSTRAP STYLESHEET

# ADD SIMPLE FORM 1/2
O Simple Form pode ser facilmente integrado ao Bootstrap 5. Bastando utilizar a opção bootstrap no gerador de instalação do simple form lançando esse codigo aqui no nosso terminal:

# ADD SIMPLE FORM 2/2
Agora podemos usar simple_form_for ao inves vez de form_with

vamos entao fazer uma rapida revisão do que vimos ontem:
esse é o codigo que precisamos escrever no nosso formulario, ou seja no nosso new da nossa aplicação rails que vai gerar o seguinte formulario HTML:
forms em rails são bastante complexos principalmente porque geramos nossos forms atraves de rails helpers como simple form que vão fazer todo o trabalho arduo de gerar todo o HTML pra gente, então para que não precisemos dedicar um dia inteiro a forms e eu matar vcs de tedio, recomendo que deem uma olhadinha da documentação de forms em rails ok?

# FIRST COMMIT

# CRUD
Aula passada

# 7 ACTIONS
na aula passada nos vimos que se fizermos resouces restaurants, nos conseguimos gerar as 7 rotas de CRUD em rails. 

# 7 ACTIONS - part 2

# SCAFFOLD
Only for demos not for projects
You never need all of the 7 CRUD actions in real projects

# vamos dar uma olhada no que o scaffold gerou pra gente:
- modelo restaurant
- nosso controller com todos os 7 metodos CRUD prontos
- nossos views icluindo nossos formularios.

Falei e repito, se vcs criarem o app de vcs hj utilizando o scaffold, nos vamos saber e vamos pedir pra vcs apagarem e começarem do zero ta?

# LAUNCH RAILS S

- USE RAILS ROUTES
- ActiveRecord::PendingMigrationError: EXPLAIN -> A MIGRAÇÃO CREATE TABLE FOI GERADA MAS NAO FOI FEITA!
rails db:migrate

Add bootstrap to forms and show pages in locahost - do crud

# SEED
rails console.
go back show restaurants on index page CHANGE THE DISPLAY

<div class="container mt-5">
  <p style="color: green"><%= notice %></p>

  <h1>Restaurants</h1>

  <div id="restaurants">
    <% @restaurants.each do |restaurant| %>
        <h6>
          <%= link_to restaurant.name, restaurant_path(restaurant)%> 
          <%= '⭐' * restaurant.rating %>
        </h6>
        <p>
          <%= restaurant.address%>
        </p>
    <% end %>
  </div>

  <%= link_to "New restaurant", new_restaurant_path %>
</div>

# BEYOND CRUD
Acontece então pessal que as vezes nos vamos querer utilizar uma rota q não seja uma das 7 CRUD de rails.

# ALL 5-STARS RESTAURANTS
como por exemplo se quisermos mostrar somente os restaurantes que tiverem 5 estrelas somente.
eu posso criar uma rota so para que o usuario possa ver todos os restaurantes que eu tenho na minha base que possuem 5 estrelas.

ENTÂO: Como obter todos os restaurantes 5 estrelas?
para isso vamos criar a seguinte rota:
GET /restaurants/top

resources :restaurants do
    collection do
        get :top
    end
end

# ONE RESTAURANT'S CHEF
vamos complicar um pouquinho agora: e se eu quiser ver o chef de um restaurante epecifico.
vamos precisar realizar alguns passos.
No nosso schema vcs podem perceber q nao temos uma coluna com o nome do chefe, então a primeira coisa que precisamos fazer é criar essa coluna.

rails generate migration AddChefNameToRestaurants chef_name:string
rails db:migrate

Agora que nos ja temos o nome do chef adicionado à nossa tabela, Como obter informações do chef de um restaurante? Qual rota vamos criar para isso?
Percebam o seguinte -> o chefe pertence a um restaurante, portanto vamos precisar de um id, ou seja, vamos precisar encontrar um restaurante primeiro antes de buscar as informações do chefe.

GET /restaurants/42/chef

Como vamos precisar de um id, aqui nos não vamos usar o metodo collection ma vamos utilizar outro chamado member.
    member do
        get :chef
    end

# NESTED RESOURCES

Aqui, nos queremos permitir que os usuários deixem um comentário sobre um restaurante e que esses comentarios sejam exibidos na página do proprio restaurante.

Pra isso vamos iniciar um novo processo, CRUD - pois vamos precisar:
- criar uma tabela REVIEWS (content:text, restaurant:references)
- fazer a migração dessa nova tabela
- adicionar validações
- adicionar associoações
- criar nossas rotas reviews
- criar nossos metodos no controller
- criar nossos views

# MODELS

# EW REVIEW
How to get the review form?

GET /restaurants/:id/reviews/new
# ROUTE
  resources :restaurants do
    resources :reviews, only: [:new]
  end


# CONTROLLER
rails g controller reviews new

 def new
    # We need @restaurant in our `simple_form_for`
    @restaurant = Restaurant.find(params[:restaurant_id])
    @review = Review.new
  end

Did you mean?  restaurant_path WE NEED A POST!!! -> CREATE

# CREATE REVIEW
Como fazer o post do formulário de avaliação?
POST /restaurants/:id/reviews
# ROUTE
resources :reviews, only: [:new, :create]

# Controller

# View
no show page do restaurante

# validations with errors

# DESTROY REVIEW
How to delete a review?
DELETE /reviews/:id

# ROUTE
Rails.application.routes.draw do
  resources :restaurants do
    resources :reviews, only: [:new, :create]
  end
  resources :reviews, only: [:destroy]
end