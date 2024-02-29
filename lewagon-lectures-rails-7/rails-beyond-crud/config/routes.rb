Rails.application.routes.draw do
  get 'reviews/new'
  resources :restaurants do
    resources :reviews, only: [:new, :create]
    collection do
      # /restaurants/top
      # get 'top', to: 'restaurants#top', as: :top_restaurants

      # get :top # vai gerar '/restaurants/top'
      # get '/balance', to: 'balances#controller'
      get :top
    end

    member do
      # /restaurants/:id/chef
      get :chef
    end

  end
  resources :reviews, only: [:destroy]
end


# COLLECTION - não precisamos de um id
# collection é um método em rails que nos permite
# para criar novas rotas dentro do contexto em que estamos:
# dentro de resources restaurantes (dentro resources)