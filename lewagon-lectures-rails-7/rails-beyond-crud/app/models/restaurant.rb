class Restaurant < ApplicationRecord
    has_many :reviews, dependent: :destroy
    # nos permite buscar todos os reviews de um restaurante -> @restaurant.reviews

    validates :content, presence: true
end
