class myheap :
     def __init__( self, maxSize ):
        self._elements = Array( maxSize )
        self._count = 0
      
        def __len__( self ):
         return self._count
          
         def capacity( self ):
           return len( self._elements )
             
              
         def add( self, value ):
            assert self._count < self.capacity(), "Cannot add to a full heap."
            self._elements[ self._count ] = value
            self._count += 1
            self._siftUp( self._count - 1 )
                
        def extract( self ):
          assert self._count > 0, "Cannot extract from an empty heap."
           # Save the root value and copy the last heap value to the root.
          value = self._elements[0]
          elf._count -= 1
          self._elements[0] = self._elements[ self._count ]
           
          self._siftDown( 0 )
           
            # Sift the value at the ndx element up the tree.
          def _siftUp( self, ndx ):
               if ndx > 0 :
                  parent = ndx // 2
                  if self._elements[ndx] > self._elements[parent] : # swap elements
                     tmp = self._elements[ndx]
                     self._elements[ndx] = self._elements[parent]
                     self._elements[parent] = tmp
                     self._siftUp( parent )
                    
                    # Sift the value at the ndx element down the tree.
                     def _siftDown( self, ndx ):
                        left = 2 * ndx + 1
                        right = 2 * ndx + 2
                        # Determine which node contains the larger value.
                        largest = ndx
                        if left < count and self._elements[left] >= self._elements[largest] :
                           largest = left
                        elif right < count and self._elements[right] >= self._elements[largest]:
                              largest = right
                              # If the largest value is not in the current node (ndx), swap it with
                              # the largest value and repeat the process.
                        if largest != ndx :
                          swap( self._elements[ndx], self._elements[largest] )
                          _siftDown( largest )
