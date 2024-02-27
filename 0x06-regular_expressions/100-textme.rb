#!/usr/bin/env ruby
string = ARGV[0]
from = string.match(/from:(?<sender>.+?)\]/)
to = string.match(/to:(?<receiver>.+?)\]/)
flags = string.match(/flags:(?<flag>.+?)\]/)
if from
  sender = from[:sender]
  if to
    receiver = to[:receiver]
    if flags
      flag = flags[:flag]
      puts "#{sender},#{receiver},#{flag}"
    end
  end
end
