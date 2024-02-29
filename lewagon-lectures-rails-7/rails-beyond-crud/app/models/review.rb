class Review < ApplicationRecord
  belongs_to :restaurant
  # nos permite chamar o restaurante pertencente a um review -> @review.restaurant
  validates :content, presence: true
end
