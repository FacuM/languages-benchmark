<?php
function lb_contains($haystack, $needle) {
  return strpos($haystack, $needle) !== false;
}

function lb_get($array, $key, $default) {
  return isset($array[$key]) ? $array[$key] : $default;
}
