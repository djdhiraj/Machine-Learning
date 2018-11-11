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
permuted_cars <- cars[sample(1:nrow(cars)),]
permuted_cars %>% head(3)
permute_rows <- function(df) df[sample(1:nrow(df)),]
permuted_cars <- cars %>% permute_rows
group_data <- function(df, n) {
 groups <- rep(1:n, each = nrow(df)/n)
 split(df, groups)
}
cars %>% permute_rows %>% group_data(5) %>% head(1)
grouped_cars <- cars %>% permute_rows %>% group_data(5)
grouped_cars[[1]]
grouped_cars[1]
grouped_cars[[1]] %>%
 lm(dist ~ speed, data = .) %>% .$coefficients

estimates <- grouped_cars[[1]] %>%
 lm(dist ~ speed, data = .) %>%
 .$coefficients
for (i in 2:length(grouped_cars)) {
 group_estimates <- grouped_cars[[i]] %>%
 lm(dist ~ speed, data = .) %>%
 .$coefficients
 estimates <- rbind(estimates, group_estimates)
}
estimates
library(purrr)
estimates <- grouped_cars %>%
 map(. %>% lm(dist ~ speed, data = .) %>% .$coefficients)
estimates
estimates <- grouped_cars %>%
 map(. %>% lm(dist ~ speed, data = .) %>% .$coefficients) %>%
 do.call("rbind", .)
estimateson
Cross Validation
cross_validation_groups <- function(grouped_df) {
 result <- vector(mode = "list", length = length(grouped_df))
 for (i in seq_along(grouped_df)) {
 result[[i]] <- grouped_df[-i] %>% do.call("rbind", .)
 }
 result
cars %>%
 permute_rows %>%
 group_data(5) %>%
 cross_validation_groups %>%
 map(. %>% lm(dist ~ speed, data = .) %>% .$coefficients) %>%  do.call("rbind", .)
cross_validation_split <- function(grouped_df) {
 result <- vector(mode = "list", length = length(grouped_df))
 for (i in seq_along(grouped_df)) {
 training <- grouped_df[-i] %>% do.call("rbind", .)
 test <- grouped_df[[i]]
 result[[i]] <- list(training = training, test = test)
 }
 result
}
cars %>%
 permute_rows %>%
 group_data(5) %>%
 cross_validation_split
prediction_accuracy_cars <- function(test_and_training) {
 result <- vector(mode = "numeric",
 length = length(test_and_training))
 for (i in seq_along(test_and_training)) {
 training <- test_and_training[[i]]$training
 test <- test_and_training[[i]]$test
 model <- training %>% lm(dist ~ speed, data = .)
 predictions <- test %>% predict(model, data = .)
 targets <- test$dist
 result[i] <- rmse(targets, predictions)
 }
 result
}
cars %>%
 permute_rows %>%
 group_data(5) %>%
 cross_validation_split %>%
 prediction_accuracy_cars
random_group <- function(n, probs) {
 probs <- probs / sum(probs)
 g <- findInterval(seq(0, 1, length = n), c(0, cumsum(probs)),
 rightmost.closed = TRUE)
 names(probs)[sample(g)]
}
random_group(8, c(training = 0.5, test = 0.5))
random_group(8, c(training = 0.5, test = 0.5))
random_group(8, c(training = 0.8, test = 0.2))

partition <- function(df, n, probs) {
 replicate(n, split(df, random_group(nrow(df), probs)), FALSE)
}
random_cars <- cars %>% partition(4, c(training = 0.5, test = 0.5))
random_cars %>% prediction_accuracy_cars








