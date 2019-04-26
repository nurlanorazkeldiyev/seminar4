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
