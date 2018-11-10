line <- cars %>% lm(dist ~ speed, data = .)
poly <- cars %>% lm(dist ~ speed + I(speed^2), data = .)
predict(line, cars) %>% head
predict(poly, cars) %>% head
rmse <- function(x,t) sqrt(mean(sum((t - x)^2)))
rmse(predict(line, cars), cars$dist)
rmse(predict(poly, cars), cars$dist)
sampled_cars <- cars %>%
  mutate(training = sample(0:1, nrow(cars), replace = TRUE))
sampled_cars %>% head
training_data <- sampled_cars %>% filter(training == 1)
test_data <- sampled_cars %>% filter(training == 0)
training_data %>% head
test_data %>% head
line <- training_data %>% lm(dist ~ speed, data = .)
poly <- training_data %>% lm(dist ~ speed + I(speed^2), data = .)
rmse(predict(line, test_data), test_data$dist)
rmse(predict(poly, test_data), test_data$dist)


