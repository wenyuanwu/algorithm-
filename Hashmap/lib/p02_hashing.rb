class Fixnum
  # Fixnum#hash already implemented for you
end

class Array
  def hash
    int = 0 
    arr = self.flatten
    arr.each_with_index do |el, idx|
      if el.is_a? Integer
        int += el*(idx+1) 
      else 
        int += (idx + 1111)
      end
    end 
    int.hash
  end
end

class String
  def hash
    int = 0 
    alphabet = ("a".."z").to_a
    self.split("").each_with_index do |char, idx|
      int += idx *alphabet.index(char.downcase)
    end 
    int.hash
  end
end

class Hash
  # This returns 0 because rspec will break if it returns nil
  # Make sure to implement an actual Hash#hash method
  def hash
    # 0
    int = 0 
    self.keys.each do |key|
      int += (key.to_s.hash + self[key].hash) 
    end 
    int.hash
  end
end
